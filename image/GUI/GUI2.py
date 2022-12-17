# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/16 16:28
# File : GUI2.py
import sys

import wx
import cv2
import numpy as np
from matplotlib import pyplot as plt, image as mpimg


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # Create a panel and a sizer
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        panel.SetSizer(sizer)
        sizer.Add(button_sizer, 0, wx.HORIZONTAL)

        # Create a button
        self.open_button = wx.Button(panel, label="打开图像")
        self.open_button.Bind(wx.EVT_BUTTON, self.OnOpen)
        button_sizer.Add(self.open_button, 0, wx.HORIZONTAL)
        # Create a button
        self.gray_button = wx.Button(panel, label="彩色转灰度")
        self.gray_button.Bind(wx.EVT_BUTTON, self.OnGray)
        button_sizer.Add(self.gray_button, 0, wx.HORIZONTAL)

        # Create a button
        self.Binary_button = wx.Button(panel, label="灰度转二值")
        self.Binary_button.Bind(wx.EVT_BUTTON, self.OnBinary)
        button_sizer.Add(self.Binary_button, 0, wx.HORIZONTAL)
        # Create a button
        self.EqualizeHist_button = wx.Button(panel, label="直方图均衡化")
        self.EqualizeHist_button.Bind(wx.EVT_BUTTON, self.OnEqualizeHist)
        button_sizer.Add(self.EqualizeHist_button, 0, wx.HORIZONTAL)
        # # Create a button
        self.Gamma_button = wx.Button(panel, label="幂律操作")
        self.gamma = 2.0
        self.Gamma_button.Bind(wx.EVT_BUTTON, self.OnGamma)
        button_sizer.Add(self.Gamma_button, 0, wx.HORIZONTAL)
        # # Create a button
        # self.BBBBB = wx.Button(panel, label="平滑滤波")
        # self.BBBBB.Bind(wx.EVT_BUTTON, self.BBBBB)
        # button_sizer.Add(self.BBBBB, 0, wx.HORIZONTAL)
        # # Create a button
        # self.BBBBB = wx.Button(panel, label="锐化")
        # self.BBBBB.Bind(wx.EVT_BUTTON, self.BBBBB)
        # button_sizer.Add(self.BBBBB, 0, wx.HORIZONTAL)
        #
        # # Create a button
        # self.BBBBB = wx.Button(panel, label="裁剪")
        # self.BBBBB.Bind(wx.EVT_BUTTON, self.BBBBB)
        # button_sizer.Add(self.BBBBB, 0, wx.HORIZONTAL)
        #
        # # Create a button
        # self.BBBBB = wx.Button(panel, label="伪彩色增强")
        # self.BBBBB.Bind(wx.EVT_BUTTON, self.BBBBB)
        # button_sizer.Add(self.BBBBB, 0, wx.HORIZONTAL)



        # Create a scrolled window
        self.scrolled_window = wx.ScrolledWindow(panel)
        sizer.Add(self.scrolled_window, 1, wx.EXPAND)


        # Bind the button to
        # Bind the button to the OnOpen method

        # Set the frame properties
        self.SetTitle("O.o")

        # Create the menu bar
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_item = file_menu.Append(wx.ID_OPEN, "打开", "打开图像文件")
        quit_item = file_menu.Append(wx.ID_EXIT, "退出", "退出程序")
        menu_bar.Append(file_menu, "文件")
        self.SetMenuBar(menu_bar)
        # Bind the Open and Quit items to the OnOpen and OnQuit methods
        self.Bind(wx.EVT_MENU, self.OnOpen, open_item)
        self.Bind(wx.EVT_MENU, self.OnQuit, quit_item)



        self.image  = None
        self.image_temp  = None



    def OnOpen(self, event):
        self.scrolled_window.DestroyChildren()

        # Show a file open dialog and get the selected file
        with wx.FileDialog(self, "打开图片", wildcard="*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = file_dialog.GetPath()
        self.image = cv2.imread(path)

        if self.image is None:
            wx.MessageBox(f"打开文件失败：{path}", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.image_temp = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)

        self.SetImageTempToPanel()

        self.scrolled_window.FitInside()
    def OnGray(self, event):
        self.scrolled_window.DestroyChildren()

        # self.image_temp = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        # self.image_temp = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)


        self.image_temp = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        self.SetImageTempToPanel()
        self.scrolled_window.FitInside()

    def OnBinary(self, event):
        self.scrolled_window.DestroyChildren()



        self.image_temp = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # 设置阈值，将图片转换为二进制图
        _, self.image_temp = cv2.threshold(self.image_temp, 127, 255, cv2.THRESH_BINARY)


        self.SetImageTempToPanel()
        self.scrolled_window.FitInside()

    def OnEqualizeHist(self, event):
        self.scrolled_window.DestroyChildren()


        self.image_temp = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # 进行直方图均衡化
        self.image_temp = cv2.equalizeHist(self.image_temp)

        self.SetImageTempToPanel()
        self.scrolled_window.FitInside()
    def OnGamma(self, event):
        self.scrolled_window.DestroyChildren()

        self.image_temp = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        self.image_temp = np.uint8(cv2.pow(self.image_temp / 255.0, self.gamma) * 255)

        # 进行直方图均衡化

        self.SetImageTempToPanel()
        self.scrolled_window.FitInside()

    def BBBBB(self):
        pass
    def OnQuit(self, event):
        self.Close()
    def SetwxImageData(self,numpyarray):
        """
        #本程序将numpyarray的数据加载到wxImage中
        #numpyarray一般从文件中读取
        #>>from matplotlib.pyplot import imread
        #>>numpyarray=imread(filename)
        #numpyarray必须是2维灰度图像或3维数组(R,G,B)
        #本程序的作用是可以将修改后的numpyarray加载到image中
        """
        nasize=len(numpyarray.shape)#测试数组的位数
        if nasize==2:
            Height,Width=numpyarray.shape
            wximage=wx.Image(Width,Height)
            Data=np.empty([Height,Width,3],dtype='byte')
            Data[:,:,0]=numpyarray
            Data[:,:,1]=numpyarray
            Data[:,:,2]=numpyarray
            wximage.SetData(Data.tobytes())
        elif nasize==3:
            Height,Width,dim=numpyarray.shape
            wximage=wx.Image(Width,Height)
            if dim==3:#保存的是(R,G,B)
                #注意下面的代码,一定要将numpyarray上下反转一下
                wximage.SetData(numpyarray)
            elif dim==4:#某些格式,较少见
                Data=np.empty([Height,Width,3],dtype='byte')
                Data[:,:,:]=numpyarray[:,:,0:3]
                wximage.SetData(Data.tobytes())
            elif dim==1:#其实仍然是灰度图像
                Data=np.empty([Height,Width,3],dtype='byte')
                Data[:,:,0]=numpyarray[:,:,0]
                Data[:,:,1]=numpyarray[:,:,0]
                Data[:,:,2]=numpyarray[:,:,0]
                wximage.SetData(Data.tobytes())
        return wximage

    def SetImageTempToPanel(self):
        _, height = self.scrolled_window.GetSize()
        width = height * self.image_temp.shape[1] / self.image_temp.shape[0]
        wx_image = self.SetwxImageData(self.image_temp)
        wx_image.Rescale(width,height)
        static_bitmap = wx.StaticBitmap(self.scrolled_window, -1, wx_image.ConvertToBitmap())
        static_bitmap.SetSizeHints(width, height, width, height)



if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None)
    screen_width, screen_height = wx.GetDisplaySize()
    frame.SetSize(screen_width, screen_height)
    frame.SetPosition((0, 0))
    frame.Show()
    app.MainLoop()
