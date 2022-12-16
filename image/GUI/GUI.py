import wx
import cv2
from matplotlib import pyplot as plt


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # Create a panel
        self.panel = wx.Panel(self)

        # Set the frame properties
        self.SetTitle("O.o")
        self.SetSize(800, 600)

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
        image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Check if the image was successfully read
        if image is None:
            # Show an error message if the image could not be read
            wx.MessageBox(f"打开文件失败：{path}", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Convert the image to a wx.Image
        wx_image = wx.Image(image.shape[1], image.shape[0])
        wx_image.SetData(image.tobytes())

        # Create a bitmap from the image and display it in the panel
        bitmap = wx_image.ConvertToBitmap()
        wx.StaticBitmap(self.panel, -1, bitmap)
        self.panel.Refresh()

        # Adjust the frame size to fit the image
        self.SetSize(image.shape[1], image.shape[0])

    def OnQuit(self, event):
        self.Close()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
