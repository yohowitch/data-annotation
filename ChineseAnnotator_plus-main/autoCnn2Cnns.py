# -*- coding: utf-8 -*-
# @Author: Terry Chan
# @Date:   2021-01-28 17:11:59
#!/usr/bin/env python
# coding=utf-8
"""用于批量转换ann文件为anns



"""



# from tkinter import *
# from tkinter.ttk import * # Frame, Button, Label, Style, Scrollbar
# from tkinter import filedialog as tkFileDialog
# from tkinter import font as tkFont
# from tkinter import messagebox as tkMessageBox

import re
from collections import deque
import pickle
import os.path
import platform
import codecs
import regex
from utils.recommend import *
import os
# import pdb
# pdb.set_trace()
from YEDDA_Annotator import getWordTagPairs

Bert_path="/home/terry/dev/model/chinese_roberta_wwm_ext_pytorch/"
    
 
# 
def readFile(filename="./data/ChineseDemo.txt.ann"):
    """读取文件
    """
    textData=[]
    for line2 in open(filename):
        # print (line2)
        # if len(line2.split(" "))==2:
        textData.append(line2)
        # else:
        #     textData.append("\n"*2)

        

    text="".join(textData)


    return text
def bulidLabel(data):
    """自动构建词典文件"""
    dict={}
    for one in data:
        for line in one:
            # print(line)
            try:
                item=line.split(" ")[1].replace("\n","")
        
                dict[item]=0
            except:
                pass
        
    print(dict)
    # !rm ./data/labels.txt
    with open('data/labels.txt','a') as f:    #设置文件对象
        for key in dict.keys():
            print(key)
            f.write(key+"\n")
    return dict


def mkdir(path):
    """[创建新的文件夹]

    Args:
        path ([str]): [文件路径]
    """
    folder=os.path.exists(path)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")

def main(file_path,seged, tagScheme, onlyNP, goldAndrecomRe,rebulidLabel=False):
    data=[]
    g = os.walk(file_path)  

    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            if "ann" in file_name and ("anns" not in file_name):
                # print(os.path.join(path, file_name) )
                # print(readFile(os.path.join(path, file_name)))
                text=readFile(os.path.join(path, file_name))
                # print(len(text.split("\n")))
                # if "Location" in text:
                #     print(os.path.join(path, file_name) )
                #     break
                # 分割后保留分隔符
                sentences=re.split(r"([。|！|？|\n])",text)
                sentences.append("")
                sentences = ["".join(i) for i in zip(sentences[0::2],sentences[1::2])]

                data=data+sentences
                
    # with open('data.txt','w') as f:    #设置文件对象
    #     for line in data[]:
    mkdir("data")
    allData=[]
    print("dev")
    with open('data/dev.txt','w') as f:    #设置文件对象

        items=data[:int(len(data)*0.15)]
        for line in items:
            # line="我觉[@得你们#症状1*]啊，你们……[@我感觉你们新闻#描述1*]界还要学习[@一个，你们非常熟悉#描述1*]西方的这一套value。"
            tagedList= getWordTagPairs(line, seged, tagScheme, onlyNP, goldAndrecomRe)
            allData.append(tagedList)
            f.write(''.join(tagedList))
            f.write("\n\n")
    print("train")
    with open('data/train.txt','w') as f:    #设置文件对象

        items=data[int(len(data)*0.15):int(len(data)*0.85)]
        for line in items:
            # print(len(line))
            # if len(line)>100:
            #     print(line)
            # line="我觉[@得你们#症状1*]啊，你们……[@我感觉你们新闻#描述1*]界还要学习[@一个，你们非常熟悉#描述1*]西方的这一套value。"
            tagedList= getWordTagPairs(line, seged, tagScheme, onlyNP, goldAndrecomRe)
            allData.append(tagedList)
            f.write(''.join(tagedList))
            f.write("\n\n")
    print("test")
    with open('data/test.txt','w') as f:    #设置文件对象
        items=data[int(len(data)*0.85):]
        for line in items:
            # line="我觉[@得你们#症状1*]啊，你们……[@我感觉你们新闻#描述1*]界还要学习[@一个，你们非常熟悉#描述1*]西方的这一套value。"
            tagedList= getWordTagPairs(line, seged, tagScheme, onlyNP, goldAndrecomRe)
            allData.append(tagedList)
            f.write(''.join(tagedList))
            f.write("\n\n")
    #创建label文件
    if rebulidLabel:
        print("label")
        print("allData",allData[:10])
        bulidLabel(allData)
if __name__ == '__main__':
    seged=True
    tagScheme="BMES"
    onlyNP=False
    goldAndrecomRe=r'\[\@.*?\#.*?\*\](?!\#)'
    # file_path="/home/terry/dev/data/药典标注后/"
    # file_path="/home/terry/dev/data/test/"
    file_path=input("anns文件目录")
    rebulidLabel=input("是否新建label（0否，1是）")
    if int(rebulidLabel) in [0,1]:
        
        main(file_path,seged, tagScheme, onlyNP, goldAndrecomRe,True)
    else:
        print("输入有错误，退出")