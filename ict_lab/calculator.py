import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 600))

        self.panel = wx.Panel(self)
        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_RIGHT)
        sizer.Add(self.text_ctrl, 0, wx.EXPAND | wx.ALL, border=10)

        buttons = [
        '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+','C' ]

        button_grid = wx.GridSizer(5, 4, 5, 5)  # Увеличиваем количество строк до 5
        for label in buttons:
            button = wx.Button(self.panel, label=label)
            button_grid.Add(button, 0, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, lambda event, label=label: self.on_button_click(label))

        sizer.Add(button_grid, 1, wx.EXPAND | wx.ALL, border=10)
        self.panel.SetSizer(sizer)

    def bind_events(self):
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_button_click(self, label):
        if label == '=':
            try:
                result = eval(self.text_ctrl.GetValue())
                self.text_ctrl.SetValue(str(result))
            except Exception as e:
                self.text_ctrl.SetValue("Error")
        elif label == 'C':
            self.text_ctrl.Clear()
        else:
            self.text_ctrl.AppendText(label)

    def on_close(self, event):
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Calculator")
    frame.Show()
    app.MainLoop()