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

# About Me

Today, over 300,000 developers worldwide use the technology our team built to process AI training data. When Google Gemini and OpenAI GPT evaluate their own capabilities, they rely on the standards we established — and ours is the only benchmark from a Chinese team in their core evaluation suites.

My path to data infrastructure started far from data itself. During my Ph.D. at [Tsinghua University](https://www.tsinghua.edu.cn/), I simulated seismic waves on a 10-million-core supercomputer and won the [Gordon Bell Prize](https://awards.acm.org/bell) — the highest award in high-performance computing. I then built real-time graph computing systems serving WeChat's billion users at Tencent, and later led a team at SenseTime building data factories that powered over 100,000 commercial models.

These experiences led me to a conviction: in the era of foundation models, the real bottleneck isn't algorithms or compute — it's data. The vast majority of human knowledge accumulated over centuries — papers, books, reports, archives — is locked in PDFs and scanned documents that large models simply cannot ingest.

So at the [Shanghai AI Laboratory](https://www.shlab.org.cn/), I founded the [OpenDataLab](https://opendatalab.com/) team to break through this barrier. We developed [MinerU ![](https://img.shields.io/github/stars/opendatalab/MinerU?style=social)](https://github.com/opendatalab/MinerU), which transforms unstructured documents into high-quality data that large models can learn from. Within a year of release, MinerU earned 50,000 GitHub stars with over 1 billion API calls, and is used in production by Google, Huawei, Alibaba, and over 100 other enterprises. Our team also curates high-quality datasets for leading models such as [InternLM](https://github.com/InternLM) and [InternVL](https://github.com/OpenGVLab/InternVL).

I have authored over 200 papers in top-tier venues, garnered <span id="total_cit">Loading...</span> citations on Google Scholar, and received honors including the [Gordon Bell Prize](https://awards.acm.org/bell), an ACL Best Theme Paper Award, and the [WAIC Yunfan Award](https://mp.weixin.qq.com/s/4xoS-GyFfQWzdUKKCP7HNQ). I'm not just doing research — I'm building the data infrastructure for the AI era.

We are hiring! I am actively seeking talented Ph.D. students, postdoctoral fellows, interns, and full-time researchers. If you are passionate about building the future of AI, I welcome you to contact me via email.


# 🚀 Impact

<div class='impact-card impact-blue' markdown="1">

### ⛏️ [MinerU](https://github.com/opendatalab/MinerU)

The world's leading open-source document parsing engine. Transforms unstructured documents into high-quality, AI-ready data for large model training.

⭐ **50,000+** GitHub Stars &nbsp;&nbsp; 📊 **1B+** API Calls &nbsp;&nbsp; 🏢 **100+** Enterprise Users (Google, Huawei, Alibaba, etc.)

</div>

<div class='impact-card impact-teal' markdown="1">

### 📏 [OmniDocBench](https://arxiv.org/abs/2412.07626)

The document parsing evaluation benchmark officially adopted by **Google Gemini** and **OpenAI GPT** — the only Chinese-team contribution in their core evaluation suites.

</div>

<div class='impact-card impact-indigo' markdown="1">

### 🌐 [OpenDataLab](https://opendatalab.com/)

Founded and leads the OpenDataLab team and open data ecosystem.

👥 **300,000+** Developers &nbsp;&nbsp; 📦 **7,000+** Datasets &nbsp;&nbsp; 🔍 **40M+** Retrievals

</div>

<div class='impact-card impact-slate' markdown="1">

### 🧠 Foundation Model Data Engine

Oversees the data pipeline for [InternLM](https://github.com/InternLM) and [InternVL](https://github.com/OpenGVLab/InternVL), processing **100PB** of raw data into **70T** high-quality tokens.

</div>


# 🔥 News
- *2026.04*: 🎉 [MinerU 2.5 Pro](https://github.com/opendatalab/MinerU) is released, achieving new SOTA on OmniDocBench v1.6! [[Tech Report](https://arxiv.org/abs/2509.22186)]
- *2026.03*: 🎉 We released [Sciverse](https://sciverse.space/), a world-leading 100PB-scale AI-Ready database for AI for Science (AI4S).
- *2026.02*: 🎉 [1](https://openreview.net/pdf?id=rIPeatvPy3) [2](https://openreview.net/pdf?id=n9wS0Hdvri) [3](https://openreview.net/pdf?id=mIO3kVDC2L) [4](https://openreview.net/pdf?id=lZlZjSxdio) [5](https://openreview.net/pdf?id=dkIXAbWuxO) [6](https://openreview.net/pdf?id=RDAhLHEHDm) [7](https://openreview.net/pdf?id=LWw9yLNQfx) papers are accepted by ICLR 2026.
- *2025.12*: 🎉 I received the Shanghai Science and Technology Youth 35 Leading Program (selected 35 scientists under the age of 35) [[News/报道](https://mp.weixin.qq.com/s/xZPx2jH0F3L51OsGuH4IaQ)]
- *2025.09*: 🎉 [MinerU 2.5](https://github.com/opendatalab/MinerU) is released! A 1.2B-parameter document parsing vision-language model that achieves state-of-the-art recognition accuracy while maintaining exceptional computational efficiency. [[Tech Report](https://arxiv.org/abs/2509.22186)] [[Model](https://huggingface.co/opendatalab/MinerU2.5-2509-1.2B)] [[GitHub](https://github.com/opendatalab/MinerU)]
- *2025.09*: 🎉 [1](https://openreview.net/pdf?id=b7bOWd3kUL) [2](https://openreview.net/pdf?id=gZjPllL9jM) [3](https://openreview.net/pdf?id=g0AMmWiHCq) [4](https://arxiv.org/abs/2503.14905) [5](https://arxiv.org/abs/2506.07227) [6](https://arxiv.org/abs/2506.07235) papers are accepted by NIPS 2025.
- *2025.07*: 🎉 I received the ACL Best Theme Paper Award [1](https://arxiv.org/pdf/2504.14194).
- *2025.07*: 🎉 I won the World Artificial Intelligence Conference Yunfan Award (one of 11 global recipients under the age of 35, 2025)
- *2025.05*: 🎉 [1](https://arxiv.org/abs/2412.17007) [2](https://arxiv.org/abs/2503.15264) [3](https://arxiv.org/abs/2412.02592) [4](https://arxiv.org/abs/2408.01812) [5](https://arxiv.org/abs/2506.10857) papers are accepted by ICCV 2025.
- *2025.05*: 🎉 [1](https://arxiv.org/abs/2503.16212) [2](https://arxiv.org/abs/2503.16212) [3](https://arxiv.org/abs/2504.12322) [4](https://arxiv.org/abs/2504.14194) [5](https://arxiv.org/abs/2503.21500) [6](https://arxiv.org/abs/2503.17439) [7](https://arxiv.org/abs/2502.11501) [8](https://arxiv.org/abs/2504.19093) [9](https://arxiv.org/abs/2402.17645) [10](https://arxiv.org/abs/2501.12273) [11](https://arxiv.org/abs/2505.12212) papers are accepted by ACL 2025.
- *2025.02*: 🎉 [1](https://arxiv.org/abs/2412.07626) [2](https://arxiv.org/abs/2501.05510) [3](https://arxiv.org/abs/2409.03643) [4](https://arxiv.org/abs/2502.20653) [5](https://cvpr.thecvf.com/virtual/2025/poster/33817) papers are accepted by CVPR 2025.
- *2025.01*: 🎉 [1] paper is accepted by NAACL 2025.
- *2025.01*: 🎉 [1](https://arxiv.org/abs/2410.09732) [2](https://arxiv.org/abs/2406.08418) [3](https://arxiv.org/abs/2409.16986) [4](https://openreview.net/pdf?id=C25SgeXWjE) [5](https://arxiv.org/abs/2310.05375) [6](https://arxiv.org/abs/2412.11863) [7](https://arxiv.org/abs/2410.17637) papers are accepted by ICLR 2025.

# 📝 Selected Research

I have authored over 200 papers with <span id="total_cit">Loading...</span> citations on [Google Scholar](https://scholar.google.com/citations?user=PopTv7kAAAAJ). Here are selected works that define my research trajectory:

**Building AI Data Infrastructure**

1. `2024` [MinerU: An Open-Source Solution for Precise Document Content Extraction](https://arxiv.org/abs/2409.18839) — Our flagship open-source document parsing engine. 50K+ GitHub stars, 1B+ API calls, adopted by 100+ enterprises. [![](https://img.shields.io/github/stars/opendatalab/MinerU?style=social)](https://github.com/opendatalab/MinerU)

2. `2024` [OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations](https://arxiv.org/abs/2412.07626) — The evaluation standard officially adopted by Google Gemini and OpenAI GPT. The only Chinese-team benchmark in their core evaluation suites.

**Award-Winning Research**

3. `SC 2017` [18.9-Pflops Nonlinear Earthquake Simulation on Sunway TaihuLight](https://ieeexplore.ieee.org/document/9926274), Haohuan Fu†, **Conghui He†**, et al. — Scaled earthquake simulations to 10 million cores, redefining the boundary of HPC applications. 🏆 **ACM Gordon Bell Prize**

4. `ACL 2025` [Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](https://arxiv.org/abs/2504.14194), Xinlin Zhuang, ..., **Conghui He†** — A principled approach to training data curation for LLMs. 🏆 **ACL Best Theme Paper Award**

**Advancing Multimodal AI**

5. `2025` [InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models](https://arxiv.org/abs/2504.10479) — Powering one of the world's leading open-source multimodal models.

6. `ICLR 2025` [OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://arxiv.org/abs/2406.08418) — A 10-billion-scale multimodal dataset advancing vision-language research.

7. `ECCV 2024` [MMBench: Is Your Multi-modal Model an All-around Player?](https://arxiv.org/abs/2307.06281) — The definitive benchmark for evaluating multimodal models. 2,000+ citations.


# 🎖 Honors
- *2026*, **Shanghai Top 35 Young Science & Technology Innovators**
- *2025*, **ACL Best Theme Paper Award** — Top 3 from 8,000+ submissions (sole corresponding author)
- *2025*, **WAIC Yunfan Award** — One of 10 global AI rising stars, World AI Conference
- *2024*, **National Distinguished Young Talent** — State-level talent program
- *2019*, **Tencent Technology Breakthrough Gold Award** — Highest technical honor, sole gold among 50+ teams
- *2017*, **ACM Gordon Bell Prize** — Highest honor in high-performance computing
- *2013*, **IEEE-IBM Smarter Planet Challenge Global Champion** — Team leader, 1st among 54 global university teams

# 🎤 Talks & Media
- *2026.03*, Invited Lecture, National Leadership Development Program, Beijing (AI & Data Theme)
- *2025.08*, CSML 2025, Session Chair & Invited Talk, Beijing
- *2025.07*, WAIC 2025 "Corpus Innovation Forum" Keynote: *MinerU2: Intelligent Engine from Heterogeneous Data to AI-Ready* · Co-keynote with CAS Academician E Weinan
- *2025.02*, Global Developer Pioneer Conference "Pujiang AI Ecosystem Forum", Shanghai
- *2023.10*, Tutorial: "An Introduction to OpenDataLab", IEEE/CVF International Conference on Computer Vision (ICCV), Paris
- *2023.06*, Tutorial: "OpenDataLab: The Next-Generation Open Dataset Platform", IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Vancouver



# 💡 Perspectives

Thoughts on AI data, open source, and building infrastructure for the next era of intelligence.

**The Data Bottleneck No One Talks About**

Everyone is racing to build bigger models, but few are asking where the data comes from. The inconvenient truth: most of human knowledge — centuries of scientific papers, legal documents, financial reports, medical records — is locked in formats that AI cannot read. PDFs, scans, handwritten notes. We solved the compute scaling problem. The data scaling problem is next, and it's harder than most people think.

**Why We Open-Sourced MinerU**

When we built MinerU, we had a choice: keep it proprietary or open-source it. We chose open source — not out of idealism, but out of strategy. Data infrastructure is like roads: the more people use them, the more valuable they become. A proprietary parsing engine serves one company. An open standard serves an industry. Within a year, 300,000 developers proved us right.

**The ROI of Data Over Architecture**

The AI industry is split between two philosophies: brute-force scaling and surgical efficiency. When Grok 3 threw 200,000 GPUs at the problem and gained 10%, while DeepSeek-R1 achieved comparable results through reinforcement learning and data distillation at a fraction of the cost, the message was clear: raw compute has diminishing returns. The real leverage is in data quality. Until we see a paradigm shift in model architecture, data optimization remains the highest-ROI path to better AI.
