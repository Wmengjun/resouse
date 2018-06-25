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
import win32api,win32con   
import ctypes


#载入文件选择框  
from adddata import * 
from operationexcel import *

global datamach
class DirList(object):
        
    def __init__(self, initdir=None):
        global datamach
#         f = open("./config.json")
#         setting = json.load(f)
#         print (setting)
#         self.startexcel("考生录入模板.xls")
        self.top = Tk()
        self.top.title('marchexcel')                    #设置标题
        self.top['bg'] = '#f0f0f0'                   #设置背景色
        self.top.geometry("500x300+600+350")         #设置窗口大小  并初始化桌面位置
        self.top.maxsize(1200,1200)                   #窗口可调整的最大值
#         self.top.attributes("-toolwind ow", 1)        #工具栏样式
        Label(self.top,text="数据适配：").grid(row=0)
        datamach = StringVar()
        datamach.set('人员，项目，子项目')
        Entry(self.top, state='readonly',textvariable = datamach).grid(row=0,column=1)
        Button(self.top,text="修改",command=self.adddata).grid(row=0,column=4)
        
        Label(self.top,text="适配 不通过",fg="red").grid(row=1,sticky=E)
        Label(self.top,text="审核结果：拒绝",fg="red").grid(row=1,column=1)
        Label(self.top,text="审核意见：数据不匹配",fg="red").grid(row=1,column=2)
        
        Label(self.top,text="审核条件：").grid(row=2)
        Label(self.top,text="工时").grid(row=2,column=1)
        Label(self.top,text="工时明细").grid(row=2,column=2)
#       Button(self.top,text="修改").grid(row=2,column=3)
        
        Button(self.top,text='上传excel', command=self.askopenfile).grid(row=3, column=0,pady=5)
        


        self.file_opt = options = {}  
        options['defaultextension'] = '.txt'  
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]  
        options['initialdir'] = 'C:\\'  
        options['initialfile'] = 'myfile.txt'  
        options['parent'] = self.top  
        options['title'] = '选择excel文件'   
    def askopenfile(self):
        path = tkf.askopenfilename(**self.file_opt)
        Data = Dataan()
        df =Data.datamach(path)
        df.to_excel(path, sheet_name='sheet0')
#         win32api.MessageBox(0, "数据审核完成，请在该"+ path +"路径下查看",win32con.MB_OK) 
        print u"数据审核完成，请在该"+ path +u"路径下查看.^_ ^"
        newpath = u"数据审核完成，请在该"+ path +u"路径下查看.^_ ^"
        ctypes.windll.user32.MessageBoxA(0,newpath.encode('gb2312'),u' 信息'.encode('gb2312'),0)
    def adddata(self):
        ad = Dir()
        datamach.set(ad.con())
        

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
