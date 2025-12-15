# 🚀 DeepLearning-Resources

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

深度学习资源整合仓库。用于收纳优质课程资料、编程作业、实战代码与学习笔记，方便持续扩展与查阅。

> **🌟 当前状态**：已完整收录 **吴恩达 Deep Learning Specialization**，正在持续添加 **PyTorch** 及更多高质量资源。

---

## 📖 目录 (Table of Contents)

- [🚀 DeepLearning-Resources](#-deeplearning-resources)
  - [📖 目录 (Table of Contents)](#-目录-table-of-contents)
  - [📂 仓库结构](#-仓库结构)
  - [📚 课程与资源](#-课程与资源)
    - [1. 吴恩达 - Deep Learning Specialization](#1-吴恩达---deep-learning-specialization)
    - [2. 优质学习笔记](#2-优质学习笔记)
  - [📝 待添加计划 (Roadmap)](#-待添加计划-roadmap)
  - [🛠️ 快速开始](#️-快速开始)
    - [1. 克隆仓库](#1-克隆仓库)
    - [2. 环境配置 (推荐 Conda)](#2-环境配置-推荐-conda)
    - [3. 启动学习](#3-启动学习)
  - [📦 环境与依赖](#-环境与依赖)
  - [💡 学习建议](#-学习建议)
  - [📅 更新日志](#-更新日志)
  - [🤝 贡献与许可](#-贡献与许可)

---

## 📂 仓库结构

```text
DeepLearning-Resources/
├── deeplearning.ai-andrewNG/   # 🇺🇸 英文原版：课件 PDF/PPT、编程作业、数据、图片
├── 吴恩达深度学习作业/          # 🇨🇳 中文版：汉化作业、Quiz 测试、补充资料
├── train_dl.ipynb              # 🧪 个人实战练习区
├── requirements.txt            # ⚙️ 项目依赖清单
└── README.md                   # 📘 说明文档
```

---

## 📚 课程与资源

这里按课程/主题整理了已收录的资源。后续添加新课程时，将遵循此格式。

### 1. 吴恩达 - Deep Learning Specialization
> **简介**: 深度学习入门必修课，涵盖从神经网络基础到序列模型的完整体系。  
> **框架**: TensorFlow / Keras

- **📂 资料路径**: 
  - 英文原版：`deeplearning.ai-andrewNG/`
  - 中文作业：`吴恩达深度学习作业/`
- **📺 视频教程**: [bilibili - 吴恩达深度学习 deeplearning.ai](https://www.bilibili.com/video/BV1FT4y1E74V?p=73&vd_source=fabe7c1b05ad19c3df47deab4ef97207)
- **🧩 课程大纲**:
  - **COURSE 1**: Neural Networks and Deep Learning（基础 / 浅层网络）
  - **COURSE 2**: Improving Deep Neural Networks（初始化 / 正则化 / 优化 / 超参）
  - **COURSE 3**: Structuring Machine Learning Projects（ML 策略）
  - **COURSE 4**: Convolutional Neural Networks（CNN / ResNets / 目标检测 / 风格迁移）
  - **COURSE 5**: Sequence Models（RNN / LSTM / 词嵌入 / 注意力）

### 2. 优质学习笔记
> **简介**: 收录网络大神整理的笔记，辅助复习与理解。

- **哥布林学者**: [《吴恩达深度学习课程》系列笔记汇总](https://home.cnblogs.com/u/Goblinscholar)

---

## 📝 待添加计划 (Roadmap)

欢迎贡献以下领域的资源：

- [ ] **PyTorch 深度学习教程** (官方教程复现 / 实战案例)
- [ ] **Transformer 与 LLM 基础** (相关论文 / Demo)
- [ ] **计算机视觉进阶** (分割 / 生成模型)

> 💡 **提示**: 新增资源时，请保持目录结构整洁，并在本 README 中添加对应说明。

---

## 🛠️ 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/BIT-Penry/DeepLearning-Resources.git
cd DeepLearning-Resources
```

### 2. 环境配置 (推荐 Conda)
```bash
# 创建虚拟环境
conda create -n dl_env python=3.8
conda activate dl_env

# 安装依赖
pip install -r requirements.txt
```
> ⚠️ **注意**: `pyaudio` 可能需要额外的系统库支持。如果安装失败可暂时跳过，仅影响序列模型中的音频处理作业。

### 3. 启动学习
```bash
jupyter notebook
```
在浏览器中导航至对应课程目录，打开 `.ipynb` 文件即可开始。  
**提示**: 移动作业文件时，请务必保留其所在文件夹的完整结构（包含 `images/`, `datasets/` 等），否则会导致报错。

---

## 📦 环境与依赖

本项目主要基于以下技术栈：

| 类别 | 库/工具 |
| :--- | :--- |
| **深度学习** | `tensorflow`, `keras` (未来将增加 `torch`) |
| **科学计算** | `numpy`, `scipy`, `pandas`, `scikit-learn` |
| **可视化** | `matplotlib` |
| **工具/处理** | `h5py`, `pillow`, `tqdm`, `opencv-python` |

完整列表请参阅 [requirements.txt](requirements.txt)。

---

## 💡 学习建议

1.  **循序渐进**: 课程设计有前后依赖，建议按 `COURSE 1` -> `COURSE 5` 的顺序学习。
2.  **动手实践**: 不要只看视频，务必亲自运行并完成 `.ipynb` 中的作业，这是理解数学推导的关键。
3.  **善用 Quiz**: 每周的 Quiz 是检查理论掌握程度的最好方式。
4.  **笔记复盘**: 结合仓库中的课件 PDF 和外部优质笔记进行复习。

---

## 📅 更新日志

- **2025-12-15**: 新增哥布林学者笔记链接。
- **2025-12-09**: 仓库初始化，完整整合吴恩达 Deep Learning Specialization（中/英双版）。

---

## 🤝 贡献与许可

- **贡献**: 欢迎提交 Issue 或 Pull Request 分享更多深度学习资源！
- **许可**: 本仓库内容仅供个人学习使用。课程资料版权归 **deeplearning.ai** 与 **Coursera** 所有。

**Happy Learning! 🎓**
