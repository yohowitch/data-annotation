中文自然语言处理 (NLP) 标注工具，与 有志之士 共同 促进 中文 自然语言处理 的 发展。



使用bert分词方案，请下载对应bert模型并且
https://www.kaggle.com/terrychanorg/chinese-roberta-wwm-ext-pytorch



## 一、关于
- 这个项目最原始的代码是从 YEDA fork 过来的，访问 [YEDA](https://github.com/jiesutd/YEDDA) 项目，了解更多信息
- 这 **不是** 一个 web 应用，而是一个基于 Python tkinter 的轻量级桌面端应用
- 本项目仅支持 Python 3.x，**不考虑** 兼容 Python 2.x
- 本项目目前仅支持实体标注，未来将加入更多功能

## 二、使用指南

### 安装 Python 3.x

### 下载本项目

`git clone https://github.com/SophonPlus/ChineseAnnotator.git` 或直接下载 [压缩包](https://github.com/SophonPlus/ChineseAnnotator/archive/master.zip) 并解压

### 开始标注
![alt text](https://github.com/SophonPlus/ChineseAnnotator/blob/master/EnglishInterface.png "标注英文")
![alt text](https://github.com/SophonPlus/ChineseAnnotator/blob/master/ChineseInterface.png "标注中文")

- 执行 `python YEDDA_Annotator.py`，启动标注程序
- 在标注程序界面的右侧，设置快捷键，如 `a: Action; b: Loc; c: Cont`
- 点击 `ReMap` 按钮，保存快捷键设置
- 点击 `Open` 按钮，选择文件 (后缀必须为 .txt 或 .ann)
- 选中文本，然后使用设置好的快捷键进行标注，标注格式形如 `[@the text span＃Location*]`
- 通过 `RMOn` 和 `RMOff` 按钮，可以开启或关闭智能推荐
- 智能推荐会根据已经手动标注的数据，自动标注未标注的数据。其格式为 `[$the text span＃Location*]`，并用绿色展示出来（注意：手动标注以 `[@` 打头，而推荐标注则以 `[$` 打头）
- 标注结果与原始文件保存在同一个目录中，文件名为 ***"原文件名 + .ann"***

### 管理标注工作
![alt text](https://github.com/SophonPlus/ChineseAnnotator/blob/master/AdminInterface.png "管理员界面")

- 执行 `python YEDDA_Admin.py`，启动管理程序
- 点击 `多人标注分析`，然后选择多个 `*.ann` 文件，会给出不同标注结果的 F 值矩阵
 ![alt text](https://github.com/SophonPlus/ChineseAnnotator/blob/master/resultMatrix.png "结果矩阵")
- 点击 `配对比较`，然后选择 2 个 `*.ann` 文件，会生成相应的对比报告 (报告为 `.tex` 格式，可以进一步编译为 `.pdf` 文件)。示例 pdf 报告如下：

![alt text](https://github.com/SophonPlus/ChineseAnnotator/blob/master/detailReport.png "详细报告")

### 其他（重要）功能
1. 按 `ctrl + z` 撤销最近 1 次的修改
2. 选择已经标注的实体，或将光标置于已标注的实体范围内，按其他实体类别的快捷键 (如 `x`) 更新实体类别 (与 `x` 对应的实体)，按 `q`，删除实体标注
3. 选择已标注的文本，如 `[@美国＃Location*]`, 再按 `q`, 删除实体标注，即恢复到未标注的状态 (如"美国")
4. 确认/删除推荐标注的实体：将光标置于推荐标注的实体范围内，按 `y` (确认)，按 `q` (退出)
5. 点击 `export` 按钮，会将 ***".ann"*** 文件导出为同名的 ***".anns"*** 文件（存放在同一目录下）。导出文件为序列标注的格式。
  - 源代码中，参数 `self.seged` 用于控制导出的行为。如果句子由空格间隔的单词构成（英文或已分词的中文），则该值应设置为 `True`，否则应设置为 `False`（如未分词的中文）
  - 另一个参数 `self.tagScheme` 控制导出的格式，***".anns"*** 文件将使用 `BMES` 格式，如何该值为 `"BMES"`，否则导出格式为 `"BIO"`

## 三、FAQ
1. 为什么是桌面端应用？

  - 理由一：我们调研了其他的开源标注工具，包括 [brat](https://github.com/nlplab/brat) 在内的大部分工具，都有点太复杂了，难以扩展

  - 理由二：开发/维护 Web 应用，涉及到前/后端的工作，需要额外的知识和技能。我们相信在 NLP 领域，Python 的普及程度要远超 Web 开发，将项目限定在 Python 之内，能够让更多感兴趣的 NLP 业内人士参与其中，共同促进中文自然语言处理的发展

2. 你们知道一个叫 [Chinese-Annotator]( https://github.com/crownpku/Chinese-Annotator) 的项目吗？

  - 当然！我们在一开始调研中文自然语言处理标注工具的时候，就注意到这个项目了。他们在 [Wiki](https://github.com/crownpku/Chinese-Annotator/wiki/Annotator-Examples) 中，详细总结了几款有代表性的标注工具，极大地帮助了我们调研工作的开展。

  - 但是，遗憾的是，截止目前 (2018-06-22) 为止，这个工具仍然处于开发阶段，尚不可用。这让我们萌生了开始本项目的想法。我们希望一开始就提供可以使用的工具，然后再在使用过程中快速地迭代完善。

3. 为什么选择从 fork [YEDA](https://github.com/jiesutd/YEDDA) 开始？
  - 我们仔细调研了大量的标注工具，而 YEDA 可能是其中功能最简陋、代码最精简的项目了。但这恰恰是我们需要的，其他项目都太复杂，难以着手改造。

## 四、未来计划
1. 采用 brat 的文件格式
2. 采用 anafora 的可视化方式
3. 加入规则标注功能
4. 加入文本分类标注功能
5. 加入主动学习功能
6. ……

## 五、参考
| 项目 | star | fork | 最后更新 | 值得借鉴之处 |
| :---- | --- | ----- | ------- | :----------- |
| [brat](https://github.com/nlplab/brat) | 575 | 212 | 2017-11-30 | 文件格式 |
| [IEPY](https://github.com/machinalis/iepy) | 675 | 152 | 2016-10-14 | 主动学习、规则标注 |
| [anafora](https://github.com/weitechen/anafora) | 82 | 25 | 2018-05-12 | 可视化方式 |
| [Chinese-Annotator](https://github.com/crownpku/Chinese-Annotator) | 384 | 98 | 2018-03-06 | 调研/设计 文档 |
| [Prodigy](https://prodi.gy/) | - | - | - | 交互方式 |
