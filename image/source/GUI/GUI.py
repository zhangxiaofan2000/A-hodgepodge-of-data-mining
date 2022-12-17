import sys

import wx
import cv2


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
        self.button = wx.Button(panel, label="打开图像")
        button_sizer.Add(self.button, 0, wx.HORIZONTAL)
        # Create a button
        self.button2 = wx.Button(panel, label="")
        button_sizer.Add(self.button2, 0, wx.HORIZONTAL)

        # Create a scrolled window
        self.scrolled_window = wx.ScrolledWindow(panel)
        sizer.Add(self.scrolled_window, 1, wx.EXPAND)


        # Bind the button to
        # Bind the button to the OnOpen method
        self.button.Bind(wx.EVT_BUTTON, self.OnOpen)
        self.button2.Bind(wx.EVT_BUTTON, self.OnOpen)

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



    def OnOpen(self, event):
        self.scrolled_window.DestroyChildren()

        # Show a file open dialog and get the selected file
        with wx.FileDialog(self, "打开图片", wildcard="*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = file_dialog.GetPath()
        img = cv2.imread(path)

        if img is None:
            wx.MessageBox(f"打开文件失败：{path}", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        _, height = self.scrolled_window.GetSize()
        width = height * self.image.shape[1] / self.image.shape[0]


        wx_image = wx.Image(self.image.shape[1], self.image.shape[0])
        wx_image.SetData(self.image.tobytes())
        wx_image.Rescale(width,height)
        bitmap = wx_image.ConvertToBitmap()

        static_bitmap = wx.StaticBitmap(self.scrolled_window, -1, bitmap)
        static_bitmap.SetSizeHints(width, height, width, height)
        self.scrolled_window.FitInside()

    def OnQuit(self, event):
        self.Close()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None)
    screen_width, screen_height = wx.GetDisplaySize()
    frame.SetSize(screen_width, screen_height)
    frame.SetPosition((0, 0))
    frame.Show()
    app.MainLoop()
