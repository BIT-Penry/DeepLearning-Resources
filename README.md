# DeepLearning-Resources

深度学习学习资源整合仓库，用于整合学习过程中的各类课程资料、编程作业和实践代码。

> **当前状态**：本仓库正在持续更新中，目前已整合吴恩达深度学习专项课程，后续将陆续添加更多优质课程资源。

## 📚 已整合课程

### ✅ 1. 吴恩达 - Deep Learning Specialization

**状态**：✅ 已完成整合

本仓库包含 **Deep Learning Specialization** 的5门核心课程：

1. **COURSE 1: Neural Networks and Deep Learning** (神经网络与深度学习)
   - Week 1: 深度学习概论
   - Week 2: 神经网络基础（Logistic回归、Python与向量化）
   - Week 3: 浅层神经网络
   - Week 4: 深层神经网络

2. **COURSE 2: Improving Deep Neural Networks** (改善深层神经网络)
   - Week 1: 深度学习的实用层面（梯度检验、初始化、正则化）
   - Week 2: 优化算法
   - Week 3: 超参数调试、Batch正则化和程序框架（TensorFlow教程）

3. **COURSE 3: Structuring Machine Learning Projects** (结构化机器学习项目)
   - Week 1-2: 机器学习策略

4. **COURSE 4: Convolutional Neural Networks** (卷积神经网络)
   - Week 1: 卷积神经网络基础
   - Week 2: 深度卷积网络：实例探究（Keras教程、ResNets）
   - Week 3: 目标检测（YOLO算法）
   - Week 4: 特殊应用（人脸识别、神经风格转换）

5. **COURSE 5: Sequence Models** (序列模型)
   - Week 1: 循环序列模型（RNN、LSTM）
   - Week 2: 自然语言处理与词嵌入（Word2Vec、Emojify）
   - Week 3: 序列模型和注意力机制（机器翻译、触发词检测）

---

## 📋 计划添加课程

- [ ] 待添加课程 1
- [ ] 待添加课程 2
- [ ] 待添加课程 3

> 💡 **提示**：添加新课程时，请在此列表中添加，并在更新日志中记录。

---

## 📁 目录结构

```
DL/
├── deeplearning.ai-andrewNG/          # 吴恩达深度学习课程（英文原版）
│   ├── COURSE 1-5/                    # 5门课程的完整资料
│   │   ├── Week 01-04/                # 每周的课程内容
│   │   │   ├── 编程作业/              # Jupyter Notebook作业
│   │   │   ├── 课件PDF/               # 课程幻灯片
│   │   │   └── 数据集/                # 作业所需数据
│   └── README
│
├── 吴恩达深度学习作业/                 # 吴恩达深度学习课程（中文版）
│   ├── 01-05. 各门课程/               # 对应5门课程
│   │   ├── 编程作业/                  # 中文版编程作业
│   │   └── quiz小测验.pdf            # 每周小测验
│   └── 如何打开jpynb作业文件.pdf
│
├── 课程资料/                          # 补充学习资料
│   ├── Deeplearning深度学习笔记v5.6.pdf
│   ├── 深度学习作业quiz-已完成.pdf
│   └── 深度学习作业quiz-空白.pdf
│
├── [未来课程文件夹]/                   # 后续添加的课程将放在这里
│
├── requirements.txt                   # Python环境依赖
├── train_dl.ipynb                     # 个人练习代码
└── README.md                          # 本文件
```

> **说明**：目录结构会随着新课程的添加而扩展，每个新课程建议创建独立的文件夹。

## 🚀 快速开始

### 环境配置

1. **克隆仓库**
   ```bash
   git clone https://github.com/BIT-Penry/DeepLearning-Resources.git
   cd DeepLearning-Resources
   ```

2. **创建虚拟环境（推荐）**
   ```bash
   # 使用 conda
   conda create -n dl_env python=3.8
   conda activate dl_env
   
   # 或使用 venv
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 或 venv\Scripts\activate  # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

   > **注意**：`pyaudio` 在某些系统上可能需要额外安装系统依赖。如果安装失败，可以暂时跳过（仅影响序列模型课程中的音频处理作业）。

### 运行作业

1. 打开 Jupyter Notebook：
   ```bash
   jupyter notebook
   ```

2. 导航到对应的课程文件夹，打开 `.ipynb` 文件开始学习。

3. **重要提示**：
   - 首次使用时，请按顺序从上到下运行每个 Cell
   - 移动作业位置时，请保持整个文件夹结构完整（包含 `images/`、`datasets/` 等资源文件夹）

## 📦 主要依赖

- **核心库**：`numpy`, `scipy`, `matplotlib`, `h5py`, `pillow`
- **深度学习框架**：`tensorflow`, `keras`
- **数据处理**：`pandas`, `scikit-learn`
- **工具库**：`tqdm`, `faker`, `babel`, `emoji`
- **音频处理**：`pydub`, `music21`, `pyaudio`（可选）
- **图像处理**：`opencv-python`

详细依赖列表请查看 [requirements.txt](requirements.txt)

## 📝 学习建议

1. **循序渐进**：按照课程顺序学习，每门课程都有前置知识要求
2. **动手实践**：完成所有编程作业，理解代码背后的数学原理
3. **做笔记**：结合课程资料中的笔记PDF，整理自己的学习笔记
4. **完成Quiz**：每周的小测验有助于巩固知识点

## 🔗 相关资源

- [Coursera 深度学习专项课程](https://www.coursera.org/specializations/deep-learning)
- [deeplearning.ai 官网](https://www.deeplearning.ai/)

## 📄 许可证

本仓库仅用于个人学习目的。课程内容版权归 deeplearning.ai 和 Coursera 所有。

## 📝 更新日志

记录课程资源的添加和更新情况：

### 2024
- ✅ **吴恩达 - Deep Learning Specialization** - 已完成整合（5门课程）

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request，共同完善学习资源！

---

**Happy Learning! 🎓**
