#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

import os
from time import sleep
from Tkinter import *
import tkFileDialog as tkf
import xlrd as xlrd
import xlwt as xlwt
import json
import io

global datamach
class Dir(object):
        
    def __init__(self, initdir=None):
        global datamach
        global en
        global root
        root = Tk()
        root.title('marchexcel')                    #设置标题
        root['bg'] = '#f0f0f0'                   #设置背景色
        root.geometry("300x50+800+400")         #设置窗口大小  并初始化桌面位置
        root.maxsize(500,500)                   #窗口可调整的最大值
        root.attributes("-toolwindow", 1)        #工具栏样式
        Label(root,text="数据适配添加：").grid(row=0)
        datamach = StringVar()
        datamach.set('人员，项目，子项目')
        en = Entry(root,textvariable = datamach)
        en.grid(row=0,column=1)
        Button(root,text="确定",command=self.delredult).grid(row=0,column=3)
        mainloop()
    def con(self):
        print(en.get())
        return en.get()
    def delredult(self):
        root.quit()
def main():
    d = Dir(os.curdir)

if __name__ == '__main__':
    main()
