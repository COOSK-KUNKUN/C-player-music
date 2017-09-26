# -*- coding: UTF-8 -*-

import wx

class mycoosk(wx.Frame):
    """docstring for mycoosk"""
    def __init__(self,parent,title ):
        super(mycoosk, self).__init__(parent, title = title , size = (320,173) )
        panel = wx.Panel(self)

        image = wx.Image("1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # wx.Image(name, type=wx.BITMAP_TYPE_ANY, index=-1)
        # 从一个文件载入一个图像


        self.button = wx.BitmapButton(panel, -1,image, pos = (10,10),size=(70,70))
        self.Bind(wx.EVT_BUTTON,self.image,self.button)
        self.button.SetDefault()
        # 载入图片的窗口
        
        self.CreateStatusBar()

        self.filemenu = wx.Menu()
        #设置菜单

        self.filemenu.Append(wx.ID_ABOUT, u"About", u"about this program")
        self.filemenu.AppendSeparator()
        self.filemenu.Append(wx.ID_ABOUT, u"exit", u"终止应用程序")
        #wx.ID_ABOUT和wx.ID_EXIT是wxWidgets提供的标准ID

        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.filemenu, u"flie")
        self.SetMenuBar(self.menuBar)
        self.Show(True)
        #创建菜单栏
               
         

    #***************************************************************************************#    
          

        

    #***************************************************************************************#    
        



    def image(self,event):
        print self.button.GetStringSelection(),' is clicked from Radio Box' 

    

app = wx.App()


frame = mycoosk(None, 'COOSK')

frame.Show()

app.MainLoop()