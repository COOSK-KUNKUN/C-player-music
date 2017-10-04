# -*- coding: UTF-8 -*-
import wx
import wx.lib.buttons as buttons
from win32com.client import Dispatch

class mycoosk(wx.Frame):
    """docstring for mycoosk"""
    def __init__(self,parent,title ):
        super(mycoosk, self).__init__(parent, title = title , size = (225,146) )
        # 窗口整体大小

        panel = wx.Panel(self)

        image_picture = wx.Image("1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # wx.Image(name, type=wx.BITMAP_TYPE_ANY, index=-1)
        # 从一个文件载入一个图像
        # 左侧头像

        self.button = wx.BitmapButton(panel, -1,image_picture, pos = (10,10),size=(70,64))
        self.Bind(wx.EVT_BUTTON,self.image,self.button)
        self.button.SetDefault()
        # 载入图片的窗口
        
        image_picture = wx.Image("1.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()

              
        ###########################################################################################
               
        self.CreateStatusBar()
        # 底部菜单栏

        ###########################################################################################
    
        # 各种图标

        image_play = wx.Image("play.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # 开始播放音乐键图标

        self.button = wx.BitmapButton(panel, -1,image_play, pos = (90,10),size=(31,31))
        self.Bind(wx.EVT_BUTTON,self.image_play,self.button)
        self.button.SetDefault()
        
        image_play = wx.Image("play.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        
        ##########################################################################

        image_stop = wx.Image("stop.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # 暂停音乐键图标

        self.button = wx.BitmapButton(panel, -1,image_stop, pos = (126,10),size=(31,31))
        self.Bind(wx.EVT_BUTTON,self.image_stop,self.button)
        self.button.SetDefault()
        
        image_play = wx.Image("stop.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        
        ##########################################################################

        image_next = wx.Image("next.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # 下一首音乐键图标

        self.button = wx.BitmapButton(panel, -1,image_next, pos = (162,45),size=(31,31))
        self.Bind(wx.EVT_BUTTON,self.image_next,self.button)
        self.button.SetDefault()
        
        image_previous = wx.Image("next.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        
        ############################################################################
        
        image_previous = wx.Image("previous.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # 上一首音乐键图标
       
        self.button = wx.BitmapButton(panel, -1,image_previous, pos = (126,45),size=(31,31))
        self.Bind(wx.EVT_BUTTON,self.image_previous,self.button)
        self.button.SetDefault()
        
        image_next = wx.Image("previous.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        
        ############################################################################

        self.open = image_open = wx.Image("open.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # 打开音乐文件键的图标
       
        self.button = wx.BitmapButton(panel, -1,image_open, pos = (90,45),size=(31,31))
        self.Bind(wx.EVT_BUTTON,self.OnOpen,self.button)
        self.button.SetDefault()
        
        image_open = wx.Image("open.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()

        #############################################################################

        self.random = image_random = wx.Image("random.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        # 随机音乐键的图标
       
        self.button = wx.BitmapButton(panel, -1,image_random, pos = (162,10),size=(31,31))
        self.Bind(wx.EVT_BUTTON,self.image_random,self.button)
        self.button.SetDefault()
        
        image_open = wx.Image("random.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()

        ###########################################################################################
        
        # 各种事件

        self.wmp=Dispatch('WMPlayer.OCX')

        ############################################################################################



    def image(self,event):
        pass

    def image_play(self,event):       
        self.wmp.controls.play()
        # WMP控件编程
        # 参考 ： http://blog.csdn.net/u014605728/article/details/50973259

        self.wmp.settings.setMode("loop", True)
        # 列表循环播放
        

        pass   

    def image_stop(self,event):
        self.wmp.controls.pause()     
        pass

    def image_previous(self,event):
        self.wmp.controls.previous()
        pass

    def image_next(self,event):
        self.wmp.controls.next()
        pass

    def OnOpen(self,event):
        FileDialog = wx.FileDialog(None, 'open', wildcard='MP3 (*.mp3)|*.mp3|''WAV (*.wav)|*.wav',style = wx.FD_MULTIPLE)
        if FileDialog.ShowModal() == wx.ID_OK:
        # ShowModal() 显示对话框.
        # 如果用户单击OK按钮返回wx.ID_OK，否则 wx.ID_CANCEL
            
            self.filename=FileDialog.GetPath()
            if self.filename:
                media=self.wmp.newMedia(self.filename)
                self.wmp.currentPlaylist.appendItem(media)
                # 添加音乐文件到列表中           
            FileDialog.Destroy()

        pass

    def image_random(self,event):
        self.wmp.settings.setMode("shuffle", True)
        pass


app = wx.App()

frame = mycoosk(None, 'COOSK')

frame.Show()

app.MainLoop()