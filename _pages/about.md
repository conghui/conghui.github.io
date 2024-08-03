---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently a Research Director at SenseTime Inc., as well as a Research Scientist and PI at the Shanghai AI Laboratory. Prior to this, I worked at WeChat as a Senior Researcher, where I initiated and developed the high-performance graph computing framework, [Plato](https://github.com/Tencent/plato). Before joining WeChat, I earned my PhD degree (2013-2018) from the Department of Computer Science at Tsinghua University under the supervision of Prof. [Haohuan Fu](http://47.94.243.94/mediawiki/index.php/Haohuan_Fu), and my Bachelor's degree (2009-2013) from the Department of Software Engineering at Sun Yat-Sen University.

My research interests include High Performance Computing, Computer Vision, and Large Language Models. In 2017, I was honored with the [Gordon Bell Prize](https://awards.acm.org/bell) , which is the highest distinction in the high-performance computing application domain. Currently, I lead the [OpenDataLab](https://opendatalab.com/) team, which aims to build an influential open dataset platform that facilitates the development, analysis and research of Artificial General Intelligence (AGI). Additionally, I oversee a data team that collects and curates massive datasets for large language models.

At SenseTime and the Shanghai AI Laboratory, we are actively hiring PhDs, postdocs, interns, and full-time researchers. If you're interested in joining our team, please feel free to reach out to me via email.

# 🔥 News
- *2024.07*: &nbsp;🎉 4 papers are accepted by ECCV 2024.
- *2024.05*: &nbsp;🎉 1 paper is accepted by ICML 2024.
- *2024.05*: &nbsp;🎉 2 papers are accepted by ACL 2024.
- *2024.03*: &nbsp; We release [Wanjuan-CC](https://opendatalab.com/OpenDataLab/WanJuanCC), a safe and high-quality Webtext dataset.
- *2024.02*: &nbsp;🎉 3 papers are accepted by CVPR 2024.
- *2023.09*: &nbsp; We release [InternLM2](https://github.com/InternLM/InternLM). See [arXiv](https://arxiv.org/abs/2403.17297) for details.
- *2023.09*: &nbsp;🎉 [VIGC](https://opendatalab.github.io/VIGC/) is accepted by AAAI 2024.
- *2023.08*: &nbsp; We release [Wanjuan 1.0](https://opendatalab.com/OpenDataLab/WanJuan1_dot_0), a large-scale multi-modal dataset for pretraining.
- *2023.06*: &nbsp; We release [InternLM](https://github.com/InternLM/InternLM). You can find technical report [here](https://github.com/InternLM/InternLM-techreport/blob/main/InternLM.pdf).
- *2022.03*: &nbsp; We launch [OpenDataLab](https://opendatalab.com/), an open data platform that enpowers AGI.


# 💻 Projects
- [OpenDataLab](https://opendatalab.com/)[![](https://img.shields.io/github/stars/opendatalab?style=social)](https://github.com/opendatalab), an open platform that facilitates the development of AGI by sharing datasets and open-sourced tools. It hosts over 7700 datasets and provides 50+ million data retrieval services to over 40,000 developers.
- [InternLM ![](https://img.shields.io/github/stars/InternLM/InternLM?style=social)](https://github.com/InternLM/InternLM), a series of 7B and 20B base and chat models, featuring outstanding reasoning capability, 1M context window and the ability to use tools.  
- [MinerU ![](https://img.shields.io/github/stars/opendatalab/MinerU?style=social)](https://github.com/opendatalab/MinerU), a one-stop, open-sourced and high-quality data extraction tool that supports PDF, webpage and e-book extraction. It is widely used in RAG as well as in training LLMs. 
- [PDF-Extract-Kit ![](https://img.shields.io/github/stars/opendatalab/PDF-Extract-Kit?style=social)](https://github.com/opendatalab/PDF-Extract-Kit), a comprehensive toolkit for high-quality PDF content extraction library.

# 📝 Publications 

- Jiaxing Sun, Weiquan Huang, Jiang Wu, Chenya Gu, Wei Li, Songyang Zhang, Hang Yan, **Conghui He***, "Benchmarking Chinese Commonsense Reasoning of LLMs: From Chinese-Specifics to Reasoning-Memorization Correlations," in *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics*, 2024. 
- Peng Gao, Renrui Zhang, Chris Liu, Longtian Qiu, Siyuan Huang, Weifeng Lin, Shitian Zhao, Shijie Geng, Ziyi Lin, Peng Jin, Kaipeng Zhang, Wenqi Shao, Chao Xu, **Conghui He**, Junjun He, Hao Shao, Pan Lu, Hongsheng Li, Yu Qiao, "SPHINX-X: Scaling Data and Parameters for a Family of Multi-modal Large Language Models", in *Proceedings of the 38th International Conference on Machine Learning (ICML)*, 2024.
- Weijia Li, Zhenghao Hu, Lingxuan Meng, Jinwang Wang, Juepeng Zheng, Runmin Dong, **Conghui He**, Gui-Song Xia, Haohuan Fu, and Dahua Lin. "Weakly-supervised 3D Building Reconstruction from Monocular Remote Sensing Images", in *IEEE Transactions on Geoscience and Remote Sensing*, 2024.
- Weijia Li, Haote Yang, Zhenghao Hu, Juepeng Zheng, Gui-Song Xia, **Conghui He***, "3D Building Reconstruction from Monocular Remote Sensing Images with Multi-level Supervisions", in *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2024.
- Junyan Ye, Qiyan Luo, Jinhua Yu, Huaping Zhong, Zhimeng Zheng, **Conghui He**, Weijia Li, "SG-BEV: Satellite-Guided BEV Fusion for Cross-View Semantic Segmentation", in *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2024. 
- Qidong Huang, Xiaoyi Dong, Pan Zhang, Bin Wang, **Conghui He**, Jiaqi Wang, Dahua Lin, Weiming Zhang, Nenghai Yu, "Opera: Alleviating hallucination in multi-modal large language models via over-trust penalty and retrospection-allocation", in *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2024.
- Bin Wang, Fan Wu, Xiao Han, Jiahui Peng, Huaping Zhong, Pan Zhang, Xiaoyi Dong, Weijia Li, Wei Li, Jiaqi Wang, **Conghui He***, "Vigc: Visual Instruction Generation and Correction", in *Proceedings of the AAAI Conference on Artificial Intelligence*, 2024. 

- Tong Zhu, Xiaoye Qu, Daize Dong, Jiacheng Ruan, Jingqi Tong, **Conghui He**, and Yu Cheng. "LLaMA-MoE: Building Mixture-of-Experts from LLaMA with Continual Pre-training", in *arXiv preprint arXiv:2406.16554*, 2024.
- Renqiu Xia, Song Mao, Xiangchao Yan, Hongbin Zhou, Bo Zhang, Haoyang Peng, Jiahao Pi, Daocheng Fu, Wenjie Wu, Hancheng Ye, Shiyang Feng, Bin Wang, Chao Xu, **Conghui He**, Pinlong Cai, Min Dou, Botian Shi, Sheng Zhou, Yongwei Wang, Junchi Yan, Fei Wu, Yu Qiao. "DocGenome: An Open Large-scale Scientific Document Benchmark for Training and Testing Multi-modal Large Language Models", in *arXiv preprint arXiv:2406.11633*, 2024.
- Qingyun Li, Zhe Chen, Weiyun Wang, Wenhai Wang, Shenglong Ye, Zhenjiang Jin, Guanzhou Chen, Yinan He, Zhangwei Gao, Erfei Cui, Jiashuo Yu, Hao Tian, Jiasheng Zhou, Chao Xu, Bin Wang, Xingjian Wei, Wei Li, Wenjian Zhang, Bo Zhang, Pinlong Cai, Licheng Wen, Xiangchao Yan, Pei Chu, Yi Wang, Min Dou, Changyao Tian, Xizhou Zhu, Lewei Lu, Yushi Chen, Junjun He, Tong Lu, Yali Wang, Limin Wang, Dahua Lin, Yu Qiao, Botian Shi, **Conghui He***, Jifeng Dai* "OmniCorpus: An Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text", in *arXiv preprint arXiv:2406.08418*, 2024. 

- Bin Wang, Linke Ouyang, Fan Wu, Wenchang Ning, Xiao Han, Zhiyuan Zhao, Jiahui Peng, Yiying Jiang, Dahua Lin, and **Conghui He***. "DSDL: Data Set Description Language for Bridging Modalities and Tasks in AI Data", in *arXiv preprint arXiv:2405.18315*, 2024.
- Tianyi Bai, Hao Liang, Binwan Wan, Ling Yang, Bozhou Li, Yifan Wang, Bin Cui, **Conghui He***, Binhang Yuan*, and Wentao Zhang*. "A Survey of Multimodal Large Language Model from A Data-centric Perspective", in *arXiv preprint arXiv:2405.16640*, 2024. 
- Wei Li, Ren Ma, Jiang Wu, Chenya Gu, Jiahui Peng, Jinyang Len, Songyang Zhang, Hang Yan, Dahua Lin, and **Conghui He**. "FoundaBench: Evaluating Chinese Fundamental Knowledge Capabilities of Large Language Models", in *arXiv preprint arXiv:2404.18359*, 2024.
- Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi Hu, Jiapeng Luo, Zheng Ma, and others. "How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites", in *arXiv preprint arXiv:2404.16821*, 2024.
- Bin Wang, Zhuangcheng Gu, Chao Xu, Bo Zhang, Botian Shi, and **Conghui He**. "UniMERNet: A Universal Network for Real-World Mathematical Expression Recognition", in *arXiv preprint arXiv:2404.15254*, 2024.
- Xiaoyi Dong, Pan Zhang, Yuhang Zang, Yuhang Cao, Bin Wang, Linke Ouyang, Songyang Zhang, Haodong Duan, Wenwei Zhang, Yining Li, and others. "InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD", in *arXiv preprint arXiv:2404.06512*, 2024.

- Chao Pang, Jiang Wu, Jiayu Li, Yi Liu, Jiaxing Sun, Weijia Li, Xingxing Weng, Shuai Wang, Litong Feng, Gui-Song Xia, and others. "H2RSVLM: Towards Helpful and Honest Remote Sensing Large Vision Language Model", in *arXiv preprint arXiv:2403.20213*, 2024.
 
- Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen, Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi Chen, Pei Chu, Xiaoyi Dong, Haodong Duan, Qi Fan, Zhaoye Fei, Yang Gao, Jiaye Ge, Chenya Gu, Yuzhe Gu, Tao Gui, Aijia Guo, Qipeng Guo, **Conghui He**, Yingfan Hu, Ting Huang, Tao Jiang, Penglong Jiao, Zhenjiang Jin, Zhikai Lei, Jiaxing Li, Jingwen Li, Linyang Li, Shuaibin Li, Wei Li, Yining Li, Hongwei Liu, Jiangning Liu, Jiawei Hong, Kaiwen Liu, Kuikun Liu, Xiaoran Liu, Chengqi Lv, Haijun Lv, Kai Lv, Li Ma, Runyuan Ma, Zerun Ma, Wenchang Ning, Linke Ouyang, Jiantao Qiu, Yuan Qu, Fukai Shang, Yunfan Shao, Demin Song, Zifan Song, Zhihao Sui, Peng Sun, Yu Sun, Huanze Tang, Bin Wang, Guoteng Wang, Jiaqi Wang, Jiayu Wang, Rui Wang, Yudong Wang, Ziyi Wang, Xingjian Wei, Qizhen Weng, Fan Wu, Yingtong Xiong, Chao Xu, Ruiliang Xu, Hang Yan, Yirong Yan, Xiaogui Yang, Haochen Ye, Huaiyuan Ying, Jia Yu, Jing Yu, Yuhang Zang, Chuyu Zhang, Li Zhang, Pan Zhang, Peng Zhang, Ruijie Zhang, Shuo Zhang, Songyang Zhang, Wenjian Zhang, Wenwei Zhang, Xingcheng Zhang, Xinyue Zhang, Hui Zhao, Qian Zhao, Xiaomeng Zhao, Fengzhe Zhou, Zaida Zhou, Jingming Zhuo, Yicheng Zou, Xipeng Qiu, Yu Qiao, Dahua Lin, "Internlm2 technical report", in *arXiv preprint arXiv:2403.17297*, 2024. 




- Yu Sun, Dongzhan Zhou, Chen Lin, **Conghui He**, Wanli Ouyang, Han-Sen Zhong, ``LOCR: Location-Guided Transformer for Optical Character Recognition'',  arXiv preprint *arXiv:2403.02127*, 2024.

- Jiantao Qiu, Haijun Lv, Zhenjiang Jin, Rui Wang, Wenchang Ning, Jia Yu, ChaoBin Zhang, Pei Chu, Yuan Qu, Runyu Peng, Zhiyuan Zeng, Huanze Tang, Ruiliang Xu, Wei Li, Hang Yan, **Conghui He***, ``WanJuan-CC: A Safe and High-Quality Open-sourced English Webtext Dataset'',  arXiv preprint *arXiv:2402.19282*2024. 


- Shuangrui Ding, Zihan Liu, Xiaoyi Dong, Pan Zhang, Rui Qian, **Conghui He**, Dahua Lin, Jiaqi Wang, ``SongComposer: A Large Language Model for Lyric and Melody Composition in Song Generation'',  arXiv preprint *arXiv:2402.17645*

- Kai Lv, Xiaoran Liu, Qipeng Guo, Hang Yan, **Conghui He**, Xipeng Qiu, Dahua Lin, ``LongWanjuan: Towards Systematic Measurement for Long Text Quality'',  arXiv preprint *arXiv:2402.13583*


- Dinghao Yang, Bin Wang, Weijia Li, **Conghui He**, ``Exploring the User Guidance for More Accurate Building Segmentation from High-Resolution Remote Sensing Images'',  *International Journal of Applied Earth Observation and Geoinformation*vol. 126, 2024, page 103609.

- Xiaoyi Dong, Pan Zhang, Yuhang Zang, Yuhang Cao, Bin Wang, Linke Ouyang, Xilin Wei, Songyang Zhang, Haodong Duan, Maosong Cao, Wenwei Zhang, Yining Li, Hang Yan, Yang Gao, Xinyue Zhang, Wei Li, Jingwen Li, Kai Chen, **Conghui He**, Xingcheng Zhang, Yu Qiao, Dahua Lin, Jiaqi Wang, ``InternLM-XComposer2: Mastering Free-form Text-Image Composition and Comprehension in Vision-Language Large Model'',  arXiv preprint *arXiv:2401.16420*2024.

- Yiqi Lin, **Conghui He***, Alex Jinpeng Wang, Bin Wang, Weijia Li, Mike Zheng Shou, ``Parrot Captions Teach CLIP to Spot Text'',  arXiv preprint *arXiv:2312.14232*2023. 
% \textbf{(Corresponding author)}

- Zhiyuan Zhao, Bin Wang, Linke Ouyang, Xiaoyi Dong, Jiaqi Wang, **Conghui He***, ``Beyond Hallucinations: Enhancing LLMs through Hallucination-Aware Direct Preference Optimization'',  arXiv preprint *arXiv:2311.16839*2023. 
% \textbf{(Corresponding author)}

- Lin Chen, Jisong Li, Xiaoyi Dong, Pan Zhang, **Conghui He**, Jiaqi Wang, Feng Zhao, Dahua Lin, ``Sharegpt4v: Improving Large Multi-modal Models with Better Captions'',  arXiv preprint *arXiv:2311.12793*2023.

- Pan Zhang, Xiaoyi Dong, Bin Wang, Yuhang Cao, Chao Xu, Linke Ouyang, Zhiyuan Zhao, Shuangrui Ding, Songyang Zhang, Haodong Duan, Hang Yan, Xinyue Zhang, Wei Li, Jingwen Li, Kai Chen, **Conghui He**, Xingcheng Zhang, Yu Qiao, Dahua Lin, Jiaqi Wang, ``Internlm-xcomposer: A Vision-Language Large Model for Advanced Text-Image Comprehension and Composition'',  arXiv preprint *arXiv:2309.15112*2023.

- Yidong Liu, **Conghui He**, Wei Li, FuKai Shang, Jun Wang, Yao Li, Rui Xu, ``MiChao-HuaFen 1.0: A Specialized Pre-trained Corpus Dataset for Domain-specific Large Models'',  arXiv preprint *arXiv:2309.13079*2023.

- Haojie Ding, Bin Wang, Guoliang Kang, Weijia Li, **Conghui He**, Yao Zhao, Yunchao Wei, ``DropQueries: A Simple Way to Discover Comprehensive Segment Representations'',  *IEEE Transactions on Multimedia*2023.

- Zhiyuan Zhao, Linke Ouyang, Bin Wang, Siyuan Huang, Pan Zhang, Xiaoyi Dong, Jiaqi Wang, **Conghui He***, ``Mllm-dataengine: An Iterative Refinement Approach for MLLM'',  arXiv preprint *arXiv:2308.13566*2023. 
% \textbf{(Corresponding author)}

- **Conghui He**, Zhenjiang Jin, Chao Xu, Jiantao Qiu, Bin Wang, Wei Li, Hang Yan, Jiaqi Wang, Dahua Lin, ``Wanjuan: A Comprehensive Multimodal Dataset for Advancing English and Chinese Large Models'',  arXiv preprint *arXiv:2308.10755*2023.

- Yi Wang, Yinan He, Yizhuo Li, Kunchang Li, Jiashuo Yu, Xin Ma, Xinhao Li, Guo Chen, Xinyuan Chen, Yaohui Wang, **Conghui He**, Ping Luo, Ziwei Liu, Yali Wang, Limin Wang, Yu Qiao, ``Internvid: A Large-Scale Video-Text Dataset for Multimodal Understanding and Generation'',  arXiv preprint *arXiv:2307.06942*2023.

- Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, **Conghui He**, Ziwei Liu, Kai Chen, Dahua Lin, ``Mmbench: Is Your Multi-modal Model an All-Around Player?'',  arXiv preprint *arXiv:2307.06281*2023.

- Weijia Li, Wenqian Zhao, Jinhua Yu, Juepeng Zheng, **Conghui He**, Haohuan Fu, Dahua Lin, ``Joint Semantic–Geometric Learning for Polygonal Building Segmentation from High-Resolution Remote Sensing Images'',  *ISPRS Journal of Photogrammetry and Remote Sensing*vol. 201, 2023, pages 26-37.

- Yiqi Lin, Huabin Zheng, Huaping Zhong, Jinjing Zhu, Weijia Li, **Conghui He**, Lin Wang, ``Sept: Towards Scalable and Efficient Visual Pre-Training'',  *Proceedings of the AAAI Conference on Artificial Intelligence*vol. 37, no. 2, 2023.

- Peng Gao, Jiaming Han, Renrui Zhang, Ziyi Lin, Shijie Geng, Aojun Zhou, Wei Zhang, Pan Lu, **Conghui He**, Xiangyu Yue, Hongsheng Li, Yu Qiao, ``Llama-Adapter V2: Parameter-Efficient Visual Instruction Model'',  arXiv preprint *arXiv:2304.15010*2023.

- Jiaqi Wang, Pan Zhang, Tao Chu, Yuhang Cao, Yujie Zhou, Tong Wu, Bin Wang, **Conghui He**, Dahua Lin, ``V3det: Vast Vocabulary Visual Detection Dataset'',  *Proceedings of the IEEE/CVF International Conference on Computer Vision*2023.

- Weijia Li, Yawen Lai, Linning Xu, Yuanbo Xiangli, Jinhua Yu, **Conghui He***, Gui-Song Xia, Dahua Lin, ``OmniCity: Omnipotent City Understanding with Multi-Level and Multi-View Images'',  *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*2023. 
% \textbf{(Co-corresponding author)}

- Xiaosong Jia, Penghao Wu, Li Chen, Jiangwei Xie, **Conghui He**, Junchi Yan, Hongyang Li, ``Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving'',  *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*2023.

- Li Chen, Chonghao Sima, Yang Li, Zehan Zheng, Jiajie Xu, Xiangwei Geng, Hongyang Li, **Conghui He**, Jianping Shi, Yu Qiao, Junchi Yan, ``Persformer: 3D Lane Detection via Perspective Transformer and the OpenLane Benchmark'',  *European Conference on Computer Vision*Cham: Springer Nature Switzerland, 2022.

- Stephen DH Yang, Bin Wang, Weijia Li, YiQi Lin, **Conghui He**, ``Unified Interactive Image Matting'',  arXiv preprint *arXiv:2205.08324*2022.

- Dinghao Yang, Bin Wang, Weijia Li, Yiqi Lin, **Conghui He**, ``Exploring the Interactive Guidance for Unified and Effective Image Matting'',  Available at SSRN 4691082, 2022.

- Jing Shao, Siyu Chen, Yangguang Li, Kun Wang, Zhenfei Yin, Yinan He, Jianing Teng, Qinghong Sun, Mengya Gao, Jihao Liu, Gengshi Huang, Guanglu Song, Yichao Wu, Yuming Huang, Fenggang Liu, Huan Peng, Shuo Qin, Chengyu Wang, Yujie Wang, **Conghui He**, Ding Liang, Yu Liu, Fengwei Yu, Junjie Yan, Dahua Lin, Xiaogang Wang, Yu Qiao, ``Intern: A New Learning Paradigm Towards General Vision'',  arXiv preprint *arXiv:2111.08687*2021.

- Weijia Li, Wenqian Zhao, Huaping Zhong, **Conghui He***, Dahua Lin, ``Joint Semantic-Geometric Learning for Polygonal Building Segmentation'',  *Proceedings of the AAAI Conference on Artificial Intelligence*vol. 35, no. 3, 2021.

- Weijia Li, Lingxuan Meng, Jinwang Wang, **Conghui He**, Gui-Song Xia, Dahua Lin, ``3D Building Reconstruction from Monocular Remote Sensing Images'',  *Proceedings of the IEEE/CVF International Conference on Computer Vision*2021.

- Zhuoming Liu, Hao Ding, Huaping Zhong, Weijia Li, Jifeng Dai, **Conghui He**, ``Influence Selection for Active Learning'',  *Proceedings of the IEEE/CVF International Conference on Computer Vision*2021.

- Tai Wang, **Conghui He**, Zhe Wang, Jianping Shi, Dahua Lin, ``Flava: Find, Localize, Adjust and Verify to Annotate Lidar-Based Point Clouds'',  *Adjunct Proceedings of the 33rd Annual ACM Symposium on User Interface Software and Technology*2020.

- Jingheng Xu, Haohuan Fu, Wayne Luk, Lin Gan, Wen Shi, Wei Xue, Chao Yang, Yong Jiang, **Conghui He**, Guangwen Yang, ``Optimizing Finite Volume Method Solvers on Nvidia GPUs'',  *IEEE Transactions on Parallel and Distributed Systems*vol. 30, no. 12, 2019, pages 2790-2805.

- Weijia Li, **Conghui He**, Haohuan Fu, Juepeng Zheng, Runmin Dong, Maocai Xia, Le Yu, Wayne Luk, ``A Real-Time Tree Crown Detection Approach for Large-Scale Remote Sensing Images on FPGAs'',  *Remote Sensing*vol. 11, no. 9, 2019, 1025.

- Weijia Li, **Conghui He**, Jiarui Fang, Juepeng Zheng, Haohuan Fu, Le Yu, ``Semantic Segmentation-Based Building Footprint Extraction Using Very High-Resolution Satellite Images and Multi-Source GIS Data'',  *Remote Sensing*vol. 11, no. 4, 2019, 403.
% (co-first author)

- Jiarui Fang, Liandeng Li, Haohuan Fu, Jinlei Jiang, Wenlai Zhao, **Conghui He**, Xin You, Guangwen Yang, ``swcaffe: A Parallel Framework for Accelerating Deep Learning Applications on Sunway TaihuLight'',  *2018 IEEE International Conference on Cluster Computing (CLUSTER)*IEEE, 2018.

- Bingwei Chen, Haohuan Fu, Yanwen Wei, **Conghui He**, Wenqiang Zhang, Yuxuan Li, Wubin Wan, Wei Zhang, Lin Gan, Zhenguo Zhang, Guangwen Yang, Xiaofei Chen, ``Simulating the Wenchuan Earthquake with Accurate Surface Topography on Sunway TaihuLight'',  *SC18: International Conference for High Performance Computing, Networking, Storage and Analysis*IEEE, 2018.

- Liandeng Li, Jiarui Fang, Haohuan Fu, Jinlei Jiang, Wenlai Zhao, **Conghui He**, Xin You, Guangwen Yang, ``swcaffe: A Parallel Framework for Accelerating Deep Learning Applications on Sunway TaihuLight'',  *2018 IEEE International Conference on Cluster Computing (CLUSTER)*IEEE, 2018.

- Weijia Li, **Conghui He**, Jiarui Fang, Haohuan Fu, ``Semantic Segmentation Based Building Extraction Method Using Multi-Source GIS Map Datasets and Satellite Imagery'',  *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops*2018.
% (共同一作)

- Weijia Li, **Conghui He**, Wayne Luk, Haohuan Fu, ``An FPGA-Based Tree Crown Detection Approach for Remote Sensing Images'',  *The IEEE International Conference on Field-Programmable Technology*2017.

- Haohuan Fu, **Conghui He***, Bingwei Chen, et al., ``18.9-Pflops Nonlinear Earthquake Simulation on Sunway TaihuLight: Enabling Depiction of 18-Hz and 8-Meter Scenarios'',  *High Performance Computing, Networking, Storage and Analysis, SC17*2017. \textbf{(ACM Gordon Bell Prize)}
% \textbf{(Co-corresponding author)}

- **Conghui He**, Shijie Sun, Benli Li, Xiaogang Tu, Donghai Yu, ``Finding Mutual X at WeChat-Scale Social Network in Ten Minutes'',  *2019 IEEE International Conference on Big Data (Big Data)*IEEE, 2019.

- **Conghui He**, Haohuan Fu, Ce Guo, Wayne Luk, and Guangwen Yang, ``A Fully-Pipelined Hardware Design for Gaussian Mixture Models'',  *IEEE Transactions on Computers*2017.

- **Conghui He**, Haohuan Fu, Wayne Luk, Weijia Li, and Guangwen Yang, ``Exploring the Potential of Reconfigurable Platforms for Order Book Update'',  *IEEE International Conference on Field-Programmable Logic and Applications (FPL)*2017.

- Haohuan Fu, **Conghui He**, Wayne Luk, Weijia Li, and Guangwen Yang, ``A Nanosecond-level Hybrid Table Design for Financial Market Data Generators'',  *The 25th IEEE International Symposium on Field-Programmable Custom Computing Machines*2017.

- Haohuan Fu, **Conghui He**, Huabin Ruan, Itay Greenspon, Wayne Luk, Yongkang Zheng, Junfeng Liao, Qing Zhang, and Guangwen Yang, ``Accelerating Financial Market Server through Hybrid List Design'',  *Proceedings of the 2017 ACM/SIGDA International Symposium on Field-Programmable Gate Arrays*pp. 289-290.

- **Conghui He**, Haohuan Fu, Yi Shen, Robert Clapp, Guangwen Yang, ``Approximating Q Propagations for Elastic Modeling on GPUs'',  *In 79th EAGE Conference and Exhibition 2017*

- Haohuan Fu, Junfeng Liao, Wei Xue, Lanning Wang, Dexun Chen, Long Gu, Jinxiu Xu, Nan Ding, Xinliang Wang, **Conghui He**, Shizhen Xu, Yishuang Liang, Jiarui Fang, Yuanchao Xu, Weijie Zheng, Jingheng Xu, Zhen Zheng, Wanjing Wei, Xu Ji, He Zhang, Bingwei Chen, Kaiwei Li, Xiaomeng Huang, Wenguang Chen, Guangwen Yang, ``Refactoring and Optimizing the Community Atmosphere Model (CAM) on the Sunway TaihuLight Supercomputer'',  *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis*IEEE Press, 2016.

- Yushu Chen, Guangwen Yang, Xiao Ma, **Conghui He**, and Guojie Song, ``A Time-Space Domain Stereo Finite Difference Method for 3D Scalar Wave Propagation'',  *Computers \& Geosciences*vol. 96, 2016, pages 218-235.

- Bingwei Chen, **Conghui He**, Yushu Chen, Haohuan Fu, ``Full Wave Inversion Based on EnKF and Source Encoding'',  *In 2016 SEG Annual Meeting*Society of Exploration Geophysicists.

- **Conghui He**, Yushu Chen, Haohuan Fu, Guangwen Yang, ``Ensemble Full Wave Inversion with Source Encoding'',  *In 77th EAGE Conference and Exhibition 2015*

- **Conghui He**, Haohuan Fu, Bangtian Liu, Huabin Ruan, Guangwen Yang, Hui Yang, and Are Osen, ``A GPU-Based Parallel Beam Migration Design'',  *In 2015 SEG Annual Meeting*Society of Exploration Geophysicists, 2015.

- Nicholas Clinton, Le Yu, Haohuan Fu, **Conghui He**, and Peng Gong, ``Global-Scale Associations of Vegetation Phenology with Rainfall and Temperature at a High Spatio-Temporal Resolution'',  *Remote Sensing*vol. 6, no. 8, 2014, pages 7320-7338.

# 🎖 Honors and Awards
- *2023*, SenseTime Award (Sensetime's highest award, 1 team from 100 teams)
- *2021*, Outstanding Team Award at SenseTime (10 teams from 200 teams)
- *2019*, Tencent Technology Breakthrough Award - Gold Prize (highest technical award, 1 team from 50 teams)
- *2018*, Outstanding Graduate PhD Student Award
- *2017*, ACM Gordon Bell Prize (the highest award in the field of high-performance computing applications)
- *2017*, National PhD Scholarship
- *2013*, Global Champion of the IEEE-IBM Smarter Planet Challenge (Team Leader, 1/54)
- *2010*, National Scholarship

# 📖 Educations
- *2013.09 - 2018.07*, PhD, Computer Science and Technology, Tsinghua University
- *2016.11 - 2017.11*, Visiting PhD Scholar, Imperial College London
- *2016.07 - 2016.10*, Visiting PhD Scholar, Stanford University
- *2009.09 - 2013.07*, Bachelor, Software Engineering, Sun Yat-Sen University

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)
