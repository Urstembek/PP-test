import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 330))

        self.panel = wx.Panel(self)
        self.create_widgets()

    def create_widgets(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        
        self.num1_text = wx.TextCtrl(self.panel)
        self.num2_text = wx.TextCtrl(self.panel)
        self.operation_text = wx.TextCtrl(self.panel)


        self.calculate_button = wx.Button(self.panel, label="Calculate")

        
        self.result_text = wx.TextCtrl(self.panel, style=wx.TE_READONLY)

        
        sizer.Add(wx.StaticText(self.panel, label="Number 1:"), 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.num1_text, 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(wx.StaticText(self.panel, label="Number 2:"), 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.num2_text, 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(wx.StaticText(self.panel, label="Operation (+, -, *, /):"), 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.operation_text, 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.calculate_button, 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(wx.StaticText(self.panel, label="Result:"), 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.result_text, 0, wx.EXPAND | wx.ALL, border=5)

        self.panel.SetSizer(sizer)

        
        self.calculate_button.Bind(wx.EVT_BUTTON, self.calculate)

    def calculate(self, event):
        
        num1 = float(self.num1_text.GetValue())
        num2 = float(self.num2_text.GetValue())
        operation = self.operation_text.GetValue()

        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                self.result_text.SetValue("Error: Division by zero")
                return
            else:
                result = num1 / num2
        else:
            self.result_text.SetValue("Error: Invalid operation")
            return

        self.result_text.SetValue(str(result))
    def on_key_press(self, event):
        keycode = event.GetKeyCode() 
        if keycode == wx.WXK_CANCEL:  
            self.Destroy() 
        event.Skip()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Calculator")
    frame.Show()
    app.MainLoop()