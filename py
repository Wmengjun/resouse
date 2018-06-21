#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from time import sleep
from Tkinter import *
from Tix import Grid

class DirList(object):
    def __init__(self, initdir=None):
        self.top = Tk()
        self.top.title('marchexcel')                    #设置标题
        self.top['bg'] = '#f0f0f0'                   #设置背景色
        self.top.geometry("500x300+600+350")         #设置窗口大小  并初始化桌面位置
        self.top.maxsize(600,1200)                   #窗口可调整的最大值
        self.top.attributes("-toolwindow", 1)        #工具栏样式
        Label(self.top,text="数据适配：").grid(row=0)
        default_value = StringVar()
        default_value.set('人员，项目，子项目')
        Entry(self.top,textvariable = default_value).grid(row=0,column=1)
        Button(self.top,text="添加").grid(row=0,column=4)
        
        Label(self.top,text="适配 不通过").grid(row=1,sticky=E)
        Label(self.top,text="审核结果：拒绝").grid(row=1,column=1)
        Label(self.top,text="审核意见：数据不匹配").grid(row=1,column=2)
        
        Label(self.top,text="审核条件：").grid(row=2)
        Label(self.top,text="工时").grid(row=2,column=1)
        Label(self.top,text="工时明细").grid(row=2,column=2)
        Button(self.top,text="修改").grid(row=2,column=3)
        
        Button(self.top,text=' 上传excel ').grid(row=3, column=0,pady=5)


  
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
