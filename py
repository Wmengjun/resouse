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
#载入文件选择框  
from adddata import * 

global datamach
class DirList(object):
        
    def __init__(self, initdir=None):
        global datamach
#         f = open("./config.json")
#         setting = json.load(f)
#         print (setting)
        self.startexcel("考生录入模板.xls")
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
#         Button(self.top,text="修改").grid(row=2,column=3)
        
        Button(self.top,text='上传excel', command=self.askopenfile).grid(row=3, column=0,pady=5)
        


        self.file_opt = options = {}  
        options['defaultextension'] = '.txt'  
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]  
        options['initialdir'] = 'C:\\'  
        options['initialfile'] = 'myfile.txt'  
        options['parent'] = self.top  
        options['title'] = '选择excel文件'   
#         self.dir_opt = options = {}  
#         options['initialdir'] = 'C:\\'  
#         options['mustexist'] = False  
#         options['parent'] = self.top  
#         options['title'] = '选择excel文件' 
    
    def askopenfile(self):  
  
        """Returns an opened file in read mode."""  

        path = tkf.asksaveasfilename(**self.file_opt)
        wb = xlrd.open_workbook(path) #只读方式打开excel文件
#         sh = wb.sheet_by_name('sheetName') #打开“sheetName”的sheet 
#         print(sh)
        sh=wb.sheet_by_index(0) #打开第一个表
        print(sh)
        sh = wb.sheets()[0] #打开第一个表
        print(sh)
        sheetNames = wb.sheet_names() #获取所有的sheet，存入sheetNames变量
        print(sheetNames)
        value = sh.cell(0,0).value  #读取单元格的值
        print(value)
    def startexcel(self,path):  
  
        """Returns an opened file in read mode."""  

        wb = xlrd.open_workbook(path) #只读方式打开excel文件
#         sh = wb.sheet_by_name('sheetName') #打开“sheetName”的sheet 
#         print(sh)
        sh=wb.sheet_by_index(0) #打开第一个表
        print(sh)
        sh = wb.sheets()[0] #打开第一个表
        print(sh)
        sheetNames = wb.sheet_names() #获取所有的sheet，存入sheetNames变量
        print(sheetNames)
        value = sh.cell(0,0).value  #读取单元格的值
        print(value)
        
    def adddata(self):
        ad = Dir()
        datamach.set(ad.con())
        
    
#         self.cwd=StringVar(self.top)
#  
#         self.dirl = Label(self.top, fg='blue',
#             font=('Helvetica', 12, 'bold'))
#         self.dirl.pack()
#  
#         self.dirfm = Frame(self.top)
#         self.dirsb = Scrollbar(self.dirfm)
#         self.dirsb.pack(side=RIGHT, fill=Y)
#         self.dirs = Listbox(self.dirfm, height=15,
#             width=50, yscrollcommand=self.dirsb.set)
#         self.dirs.bind('<Double-1>', self.setdirandgo)
#         self.dirsb.config(command=self.dirs.yview)
#         self.dirs.pack(side=LEFT, fill=BOTH)
#         self.dirfm.pack()
#  
#         self.dirn = Entry(self.top, width=50,
#             textvariable=self.cwd)
#         self.dirn.bind('<Return>', self.dols)
#         self.dirn.pack()
#  
#         self.bfm = Frame(self.top)
#         self.clr = Button(self.bfm, text='Clear',
#             command=self.clrdir,
#             activeforeground='white',
#             activebackground='blue')
#         self.ls = Button(self.bfm,
#             text='List Directory',
#             command=self.dols,
#             activeforeground='white',
#             activebackground='green')
#         self.quit = Button(self.bfm, text='Quit',
#             command=self.top.quit,
#             activeforeground='white',
#             activebackground='red')
#         self.clr.pack(side=LEFT)
#         self.ls.pack(side=LEFT)
#         self.quit.pack(side=LEFT)
#         self.bfm.pack()
#  
#         if initdir:
#             self.cwd.set(os.curdir)
#             self.dols()
#  
#     def clrdir(self, ev=None):
#         self.cwd.set('')
#  
#     def setdirandgo(self, ev=None):
#         self.last = self.cwd.get()
#         self.dirs.config(selectbackground='red')
#         check = self.dirs.get(self.dirs.curselection())
#         if not check:
#             check = os.curdir
#         self.cwd.set(check)
#         self.dols()
#  
#     def dols(self, ev=None):
#         error = ''
#         tdir = self.cwd.get()
#         if not tdir:
#             tdir = os.curdir
#  
#         if not os.path.exists(tdir):
#             error = tdir + ': no such file'
#         elif not os.path.isdir(tdir):
#             error = tdir + ': not a directory'
#  
#         if error:
#             self.cwd.set(error)
#             self.top.update()
#             sleep(2)
#             if not (hasattr(self, 'last') \
#                 and self.last):
#                     self.last = os.curdir
#             self.cwd.set(self.last)
#             self.dirs.config(
#                 selectbackground='LightSkyBlue')
#             self.top.update()
#             return
#  
#         self.cwd.set(
#             'FETCHING DIRECTORY CONTENTS...')
#         self.top.update()
#         dirlist = os.listdir(tdir)
#         dirlist.sort()
#         os.chdir(tdir)
#         self.dirl.config(text=os.getcwd())
#         self.dirs.delete(0, END)
#         self.dirs.insert(END, os.curdir)
#         self.dirs.insert(END, os.pardir)
#         for eachFile in dirlist:
#             self.dirs.insert(END, eachFile)
#         self.cwd.set(os.curdir)
#         self.dirs.config(
#             selectbackground='LightSkyBlue')

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
