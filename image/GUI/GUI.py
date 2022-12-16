import wx
import cv2
from matplotlib import pyplot as plt


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # Replace the panel with a scrolled window
        self.scrolled_window = wx.ScrolledWindow(self, -1, style=wx.HSCROLL | wx.VSCROLL)
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

    def OnOpen(self, event):
        # Show a file open dialog and get the selected file
        with wx.FileDialog(self, "打开图片", wildcard="*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = file_dialog.GetPath()

        # Read the image file using cv2
        img = plt.imread(path)
        # 改变通道顺序
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Check if the image was successfully read
        if img is None:
            # Show an error message if the image could not be read
            wx.MessageBox(f"打开文件失败：{path}", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Convert the image to a wx.Image
        wx_image = wx.Image(img.shape[1], img.shape[0])
        wx_image.SetData(img.tobytes())

        # Create a bitmap from the image
        bitmap = wx_image.ConvertToBitmap()
        # Set the scrollbars
        self.scrolled_window.SetScrollbars(1, 1, img.shape[1], img.shape[0])

        # Create a static bitmap and add it to the scrolled window
        static_bitmap = wx.StaticBitmap(self.scrolled_window, -1, bitmap)

        static_bitmap.SetSizeHints(wx_image.GetWidth(), wx_image.GetHeight(),
                                   wx_image.GetWidth(), wx_image.GetHeight())

        self.scrolled_window.FitInside()

    def OnQuit(self, event):
        self.Close()
if __name__ == '__main__':

    app = wx.App()
    frame = MyFrame(None)
    screen_width, screen_height = wx.GetDisplaySize()
    frame.SetSize(screen_width, screen_height)
    frame.SetPosition((0, 0))
    frame.Show()
    app.MainLoop()