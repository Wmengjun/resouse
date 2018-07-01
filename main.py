#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
'''
Created on 2018年6月29日

@author: wmj
'''


import wx
from numpy import size
class Mywin(wx.Frame):
    def __init__(self, parent, title):
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
        self.Bind(wx.EVT_BUTTON, self.OnEnterPressed, self.button3)
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
        print("输出 结果")
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
