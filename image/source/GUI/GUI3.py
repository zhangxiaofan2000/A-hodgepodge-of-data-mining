import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 200))

        # 创建一个变量
        self.var = 'Hello World'

        # 创建一个按钮
        self.button = wx.Button(self, label='Show Text Entry Dialog')

        # 绑定按钮的事件处理函数
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, event):
        # 创建一个文本输入对话框
        dlg = wx.TextEntryDialog(self, 'Enter Some Text:', 'Text Entry Dialog')

        # 显示对话框
        if dlg.ShowModal() == wx.ID_OK:
            # 获取文本输入框中的文本
            text= dlg.GetValue()
        # 更新变量的值
        self.var = text

app = wx.App()
frame = MyFrame(None, 'Text Entry Dialog Demo')
frame.Show()
app.MainLoop()