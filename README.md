## 数据标注
首先非常感谢YEDDA标注工具，这里提供了YEDDA的原版和中文版，都是github开源的，还有BIO转换文件的代码也是CSDN小力水手开源的。
## 所做工作
BIO转换将YEDDA输出的文件内容转换为BIO模式，适合了我们平时的数据标注模式。这里只对BIO转换文件做了些改进，使得运行更加通畅。
## 环境
YEDDA原版： python 2.7
YEDDA中文版： python 3.x
## 运行
1. 首先运行YEDDA，注意YEDDA的输入文件格式
2. 改 BIO转换.py 输入输出文件

## 引用
@article{yang2017yedda,  
     title={YEDDA: A Lightweight Collaborative Text Span Annotation Tool},  
     author={Yang, Jie and Zhang, Yue and Li, Linwei and Li, Xingxuan},  
     booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
     url={http://aclweb.org/anthology/P18-4006},
     year={2018}  
    } 

## 思考
作者本来有想用brat，奈何brat文件需要Ubuntu，要不就是虚拟环境，实属太麻烦。所以作者推荐NLPer使用YEDDA，希望这份整理好的代码能给各位读者带来便利，别忘了星星。
