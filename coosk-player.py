# -*- coding: UTF-8 -*-

import wx
import os
import wx.lib.buttons as buttons

dirName = os.path.dirname(os.path.abspath(__file__))
bitmapCoosk = os.path.join(dirName, 'bitmaps')

class mycoosk(wx.Frame):
    """docstring for mycoosk"""
    def __init__(self,parent,title ):
        super(mycoosk, self).__init__(parent, title = title , size = (320,173) )
        panel = wx.Panel(self)

        image_picture = wx.Image("1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # wx.Image(name, type=wx.BITMAP_TYPE_ANY, index=-1)
        # 从一个文件载入一个图像

        self.button = wx.BitmapButton(panel, -1,image_picture, pos = (10,10),size=(70,64))
        self.Bind(wx.EVT_BUTTON,self.image,self.button)
        self.button.SetDefault()
        # 载入图片的窗口
        
        image_picture = wx.Image("1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()

        
        
        #***************************************************************************
               
        self.filemenu = wx.Menu()
        #设置菜单

        self.CreateStatusBar()

        self.filemenu.Append(wx.ID_ABOUT, u"打开", u"Open the music")
        self.filemenu.AppendSeparator()
        self.filemenu.Append(wx.ID_EXIT, u"退出", u"Exit the software")
        #wx.ID_ABOUT和wx.ID_EXIT是wxWidgets提供的标准ID

        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.filemenu, u"文件")
        self.SetMenuBar(self.menuBar)
        self.Show(True)
        #创建菜单栏
               
         

        #***************************************************************************************#    
    


        image_play = wx.Image("play.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()


        self.button = wx.BitmapButton(panel, -1,image_play, pos = (90,10),size=(28.6,28.6))
        self.Bind(wx.EVT_BUTTON,self.image_play,self.button)
        self.button.SetDefault()
        
        image_play = wx.Image("play.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()


        

        #***************************************************************************************#    
        



    def image(self,event):
        pass

    def image_play(self,event):
        pass   

app = wx.App()

frame = mycoosk(None, 'COOSK')

frame.Show()

app.MainLoop()