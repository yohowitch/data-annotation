# -*- coding: utf-8 -*-
# @Author: Jie Yang from SUTD
# @Date:   2016-Jan-06 17:11:59
# @Last Modified by:   Jie Yang,     Contact: jieynlp@gmail.com
# @Last Modified time: 2017-09-24 21:47:14
#!/usr/bin/env python
# coding=utf-8

from tkinter import *
from tkinter.ttk import * # Frame, Button, Label, Style, Scrollbar
from tkinter import filedialog as tkFileDialog
from tkinter import font as tkFont
from tkinter import messagebox as tkMessageBox

import re
from collections import deque
import pickle
import os.path
import platform

from utils.recommend import *
from utils.metric4ann import *
from utils.compareAnn import *


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.Version = u"YEDDA-V1.0 管理员"
        self.OS = platform.system().lower()
        self.parent = parent
        self.fileName = ""
        # 初始化 GUI 显示参数        
        self.textColumn = 3
        self.initUI()        
        
    def initUI(self):
        ## 初始化 UI	
        self.parent.title(self.Version)
        self.pack(fill=BOTH, expand=True)
        
        for idx in range(0,self.textColumn):
            if idx == 1:
                self.columnconfigure(idx, weight =10)
            else:
                self.columnconfigure(idx, weight =1)
        # for idx in range(0,2):
        #     self.rowconfigure(idx, weight =1)
        the_font=('TkDefaultFont', 18, )
        style0 = Style()
        style0.configure(".", font=the_font, )

        width_size = 30

        abtn = Button(self, text=u"多标注分析", command=self.multiFiles, width = width_size)
        abtn.grid(row=0, column=1)

        recButton = Button(self, text=u"配对比较", command=self.compareTwoFiles,  width = width_size)
        recButton.grid(row=1, column=1)

        cbtn = Button(self, text=u"退出", command=self.quit, width = width_size)
        cbtn.grid(row=2, column=1)

    def ChildWindow(self, input_list, result_matrix):
        file_list = []
        for dir_name in input_list:
            if ".ann" in dir_name:
                dir_name = dir_name[:-4]
            if "/" in dir_name:
                file_list.append(dir_name.split('/')[-1])
            else:
                file_list.append(dir_name)

        # 创建菜单
        self.popup = Menu(self.parent, tearoff=0)
        self.popup.add_command(label="Next", command=self.selection)
        self.popup.add_separator()

        def do_popup(event):
            # 显示弹出菜单
            try:
                self.popup.selection = self.tree.set(self.tree.identify_row(event.y))
                self.popup.post(event.x_root, event.y_root)
            finally:
                # make sure to release the grab (Tk 8.0a1 only)
                self.popup.grab_release()

        # 创建树状视图
        win2 = Toplevel(self.parent)
        new_element_header=file_list
        treeScroll = Scrollbar(win2)
        treeScroll.pack(side=RIGHT, fill=Y)
        title_string = "F:Entity/Chunk"
        self.tree = Treeview(win2, columns=[title_string]+file_list, show="headings")

        self.tree.heading(title_string, text=title_string, anchor=CENTER)
        self.tree.column(title_string, stretch=YES, minwidth=50, width=100, anchor=CENTER)
        for each_file in file_list:
            self.tree.heading(each_file, text=each_file, anchor=CENTER)
            self.tree.column(each_file, stretch=YES, minwidth=50, width=100, anchor=CENTER)
        for idx in range(len(file_list)):
            self.tree.insert("" ,  'end', text=file_list[idx], values=[file_list[idx]]+result_matrix[idx],  tags = ('chart',))
        the_font=('TkDefaultFont', 18, )
        self.tree.tag_configure('chart', font=the_font)
        style = Style()
        style.configure(".", font=the_font, )
        style.configure("Treeview", )
        style.configure("Treeview.Heading",font=the_font, ) #<----
        self.tree.pack(side=TOP, fill=BOTH)
        # self.tree.grid()

        self.tree.bind("<Button-3>", do_popup)

        win2.minsize(30,30)
		
    def selection(self):
        print(self.popup.selection)

    def multiFiles(self):
        ftypes = [('ann files', '.ann')]
        filez = tkFileDialog.askopenfilenames(parent=self.parent, filetypes = ftypes, title='Choose a file')
        if len(filez) < 2:
            tkMessageBox.showinfo(u"监视错误", u"不足 2 个文件！\n\n请至少选择 2 个文件！")
        else:
            result_matrix =  generate_report_from_list(filez)
            self.ChildWindow(filez, result_matrix)

    def compareTwoFiles(self):
        ftypes = [('ann files', '.ann')]
        filez = tkFileDialog.askopenfilenames(parent=self.parent, filetypes = ftypes, title=u'选择文件')
        if len(filez) != 2:
            tkMessageBox.showinfo(u"比较错误", u"请选择 2 个文件！")
        else:
            f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".tex")
            write_result = compareBoundary(filez[0],filez[1],f)
            if write_result:
                tkMessageBox.showinfo(u"生成 Latex", u"成功生成 Latex 文件！\n\保存到 "+ f.name)
                # import os
                # os.system("pdflatex "+ f.name)
            else:
                tkMessageBox.showinfo(u"Latex 错误", u"生成 Latex 错误：2 个文件的句子数不相等！")
            f.close()


def main():
    print(u"启动 YEDDA 管理员程序！")
    print((u"操作系统：%s")%(platform.system()))
    root = Tk()
    root.geometry("400x100")
    app = Example(root)
    
    root.mainloop()
	

if __name__ == '__main__':
    main()