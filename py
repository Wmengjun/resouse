#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

import os
from tkinter import *  
from tkinter import ttk
from tkinter.filedialog import *
import json
import ctypes as ctypes
import pandas as pd
import numpy as np
from base64 import decode, encode
import codecs



global datamach
class DirList(object):
        
    def __init__(self, initdir=None):
        global datamach
        global name
#         加载json 文件数据
        json_data=codecs.open("./config.json","r","utf-8").read()

        data = json.loads(json_data)
        print(data)
        temp=[]
        for newdata in data:
            print(newdata)
            temp.append(data[newdata])
            print(temp)

#         data = json.load(f)
#         print(dict)
        self.top = Tk()
        self.top.title('marchexcel')                    #设置标题
        self.top['bg'] = '#f0f0f0'                   #设置背景色
        self.top.geometry("500x300+600+350")         #设置窗口大小  并初始化桌面位置
        self.top.maxsize(1200,1200)                   #窗口可调整的最大值
        Label(self.top,text="模板文件:").grid(row=0,column=2)
        self.name = StringVar()
        self.name.set('./模板.xlsx')
        Entry(self.top, state='readonly', width=30,textvariable = self.name,).grid(row=0,column=3)
        Button(self.top,text='...' ,  command=self.machaskopenfile).grid(row=0, column=4,pady=5)
        datamach = StringVar()
        datamach.set('')
        Label(self.top,text="适配文件:").grid(row=1,column=2)
        Entry(self.top, state='readonly', width=30,textvariable = datamach,).grid(row=1,column=3)
        Button(self.top,text='...' ,  command=self.askopenfile).grid(row=1, column=4,pady=5)
        Button(self.top,text='生成', command=self.mach).grid(row=3, column=3,pady=5)
        


        self.file_opt = options = {}  
        options['defaultextension'] = '.txt'  
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]  
        options['initialdir'] = './'  
        options['initialfile'] = '.xlsx'  
        options['parent'] = self.top  
        options['title'] = '选择excel文件'   
    def askopenfile(self):
        global datamach
        self.filepath = askopenfilenames(**self.file_opt )
        datamach.set(self.filepath)
        print(self.filepath)
    def machaskopenfile(self):
        global name
        self.matchfilepath = askopenfilenames(**self.file_opt )
        name.set(self.matchfilepath)
        print(self.matchfilepath)
        
    def mach(self):
        print(self.name.get())
        df =self.datamach(self.filepath, self.name.get())
        df.to_excel(str(self.filepath[0]), sheet_name='sheet0')
        newpath = "数据审核完成，请在该"+ str(self.filepath[0]) +"路径下查看.^_ ^"
        ctypes.windll.user32.MessageBoxA(0,newpath.encode('gb2312'),' 信息'.encode('gb2312'),0)
#        
    def show_msg(self,*args):
        print(self.players.get())
        
    def datamach(self,path,modelpath):
        print(path[0])
        print(modelpath[0])
        self.modeldf = pd.DataFrame(pd.read_excel(str(modelpath[0])))
        self.df = pd.DataFrame(pd.read_excel(str(path[0])))
        for i in range(self.df.shape[0]):
#             print str(self.modeldf.ix[i,'工时明细']).find('e')
            if (self.modeldf.ix[i,'项目']!=self.df.ix[i,'项目']) |\
            (self.modeldf.ix[i,'子项目']!=self.df.ix[i,'子项目'])|\
            (self.modeldf.ix[i,'申报人']!=self.df.ix[i,'申报人']):
                self.df.ix[i,'审批结果'] = '拒绝'
                self.df.ix[i,'审批意见'] = '项目错误'
            elif self.modeldf.ix[i,'工时']!=self.df.ix[i,'工时']:
                self.df.ix[i,'审批结果'] = '拒绝'
                self.df.ix[i,'审批意见'] = '工时时间不正确'
            elif self.modeldf.ix[i,'工时明细'][:(str(self.modeldf.ix[i,'工时明细']).find('remark'))+1]!=\
            self.df.ix[i,'工时明细'][:(str(self.df.ix[i,'工时明细']).find('remark'))+1]:
                self.df.ix[i,'审批结果'] = '拒绝'
                self.df.ix[i,'审批意见'] = '工时活动错误'
            else:
                self.df.ix[i,'审批结果'] = '通过'
                self.df.ix[i,'审批意见'] = 'ok'
        print (self.df)
        return self.df

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
