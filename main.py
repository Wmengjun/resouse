#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018年6月29日

@author: wmj
'''


import wx
from numpy import size
import json
import os
import codecs
import pandas as pd
class Mywin(wx.Frame):
    def __init__(self, parent, title):
#             ctypes.windll.user32.MessageBoxA(0,"同目录下config.json 文件不存在".encode('gb2312'),' 信息'.encode('gb2312'),0)
        super(Mywin, self).__init__(parent, title = title)
#         菜单栏
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
 
        self.menu_select = menu1.Append(-1, '退出') #快捷键
        self.Bind(wx.EVT_MENU, self.about, self.menu_select)
        menuBar.Append(menu1, '文件')
        menu2 = wx.Menu()
        self.menu_op = menu2.Append(-1, '说明') #快捷键
        self.Bind(wx.EVT_MENU, self.onSelect, self.menu_op)
        menuBar.Append(menu2, '关于')
        self.SetMenuBar(menuBar)
#     操作区
        panel = wx.Panel(self, -1) 
        #创建 垂直尺寸管理器 : 用来管理接下来的 水平管理器 和 其他组件
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        stctext1 =wx.StaticText(panel, -1, "模板文件：", (20, 10))
        self.t1 = wx.TextCtrl(panel,value='./模板.xlsx')
        self.button1 = wx.Button(panel,1,"...",size=(20,20))
        self.Bind(wx.EVT_BUTTON, self.OnEnterPressed, self.button1)
        self.button1.SetDefault()
        hbox1.Add(stctext1, proportion = 0, flag = wx.EXPAND|wx.ALL, border = 5)
        hbox1.Add(self.t1, proportion = 1, flag = wx.EXPAND|wx.ALL, border = 5)
        hbox1.Add(self.button1, proportion = 0, flag = wx.EXPAND|wx.ALL, border = 5)
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
        stctext2 =wx.StaticText(panel, -1, "适配文件：", (20, 10))
        self.t2 = wx.TextCtrl(panel,value ='')
        self.button2 = wx.Button(panel,2,"...",size=(20,20))
        self.Bind(wx.EVT_BUTTON, self.OnEnterPressed, self.button2)
        self.button2.SetDefault()
        hbox2.Add(stctext2, proportion = 0, flag = wx.EXPAND|wx.ALL, border = 5)
        hbox2.Add(self.t2, proportion = 1, flag = wx.EXPAND|wx.ALL, border = 5)
        hbox2.Add(self.button2, proportion = 0, flag = wx.EXPAND|wx.ALL, border = 5)
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.button3 = wx.Button(panel, -1,"生成目标文件" ,)
        self.Bind(wx.EVT_BUTTON, self.getnewfiles, self.button3)
        self.button3.SetDefault()
        hbox3.Add(self.button3, proportion = 0, flag = wx.EXPAND|wx.ALL, border = 5)


        #将 hbox1 、 hbox2 、hbox3 添加到 vbox 上
        vbox.Add(hbox1, proportion=0, flag=wx.EXPAND | wx.ALL, border=0)
        vbox.Add(hbox2, proportion=0, flag=wx.EXPAND | wx.ALL, border=0)
        vbox.Add(hbox3, proportion=0, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=5)
        #设置 面板 panel 的尺寸管理器为 vbox
        panel.SetSizer(vbox)

        #调整 窗口框架 并显示
        self.SetSize((600,500))
        self.Center()
        self.Show()
        self.Fit()
        
    def OnEnterPressed(self, event):
        print(event.GetId())
        wildcard = "All files (*.*)|*.*"
        dlg = wx.FileDialog(self,"选择excel文件",wildcard =wildcard,style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            if event.GetId()==1:
                self.t1.SetValue(dlg.GetPath())
            else:
                self.t2.SetValue(dlg.GetPath())
            print (dlg.GetPath()) #文件夹路径
        dlg.Destroy()
    def getnewfiles(self,event):
        if os.path.exists('./config.json'):
            json_data=codecs.open("./config.json","r","utf-8").read()
            self.data = json.loads(json_data)
        else:
            dlg=wx.MessageDialog(None,"同目录下config.json 文件不存在","异常",wx.OK|wx.ICON_QUESTION)
            result=dlg.ShowModal()
            dlg.Destroy()
        if os.path.exists(self.t2.GetValue()):
            self.df = pd.DataFrame(pd.read_excel(str(self.t2.GetValue())))
        else:
            dlg=wx.MessageDialog(None,"适配文件不存在","异常",wx.OK|wx.ICON_QUESTION)
            result=dlg.ShowModal()
            dlg.Destroy()
        if os.path.exists(self.t1.GetValue()):
            self.modeldf = pd.DataFrame(pd.read_excel(str(self.t1.GetValue())))
        else:
            dlg=wx.MessageDialog(None,"模板文件不存在","异常",wx.OK|wx.ICON_QUESTION)
            result=dlg.ShowModal()
            dlg.Destroy()
        
        
        for i in range(self.df.shape[0]):
            if (str(self.modeldf.ix[i,'项目']).lower().lstrip()!=str(self.df.ix[i,'项目']).lower().lstrip()) |\
            (str(self.modeldf.ix[i,'子项目']).lower().lstrip()!=str(self.df.ix[i,'子项目']).lower().lstrip())|\
            (str(self.modeldf.ix[i,'申报人']).lower().lstrip()!=str(self.df.ix[i,'申报人']).lower().lstrip()):
                self.df.ix[i,'审批结果*'] = self.data["errorresult"]
                self.df.ix[i,'审批意见*'] = self.data["opinion1"]
            elif self.modeldf.ix[i,'工时']!=self.df.ix[i,'工时']:
                self.df.ix[i,'审批结果*'] = self.data["errorresult"]
                self.df.ix[i,'审批意见*'] = self.data["opinion2"]
            elif str(self.modeldf.ix[i,'工时明细'][:(str(self.modeldf.ix[i,'工时明细']).find('remark'))]).lower().lstrip()!=\
            str(self.df.ix[i,'工时明细'][:(str(self.df.ix[i,'工时明细']).find('remark'))]).lower().lstrip():
                self.df.ix[i,'审批结果*'] = self.data["errorresult"]
                self.df.ix[i,'审批意见*'] = self.data["opinion3"]
            else:
                self.df.ix[i,'审批结果*'] = self.data["rightresult"]
                self.df.ix[i,'审批意见*'] = self.data["opinion4"]
        print(self.df)
        try:
            self.df.to_excel(self.t2.GetValue(), sheet_name='sheet0')
            newpath = "数据审核完成，请在该"+ self.t2.GetValue() +"路径下查看.^_ ^"
            dlg=wx.MessageDialog(None,newpath,"信息",wx.OK|wx.ICON_QUESTION)
            result=dlg.ShowModal()
            dlg.Destroy()
        except:
            dlg=wx.MessageDialog(None,"文件打开，不能进行读写操作","异常",wx.OK|wx.ICON_QUESTION)
            result=dlg.ShowModal()
            dlg.Destroy()
    def onSelect(self, event):
        dlg=wx.MessageDialog(None,"应用同目录下不可删除配置文件，否则会出现异常","说明",wx.OK|wx.ICON_QUESTION)
        result=dlg.ShowModal()
        dlg.Destroy()
    def about(self, event):
        wx.GetApp().ExitMainLoop()

def main():
    #设置了主窗口的初始大小960x540 800x450 640x360
    app = wx.App()
    Mywin(None, "工时审批")
    app.MainLoop()

if __name__ == '__main__':
    main()
