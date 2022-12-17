from  GUI2 import *


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    screen_width, screen_height = wx.GetDisplaySize()
    frame.SetSize(screen_width, screen_height)
    frame.SetPosition((0, 0))
    frame.Show()
    app.MainLoop()