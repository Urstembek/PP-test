import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 330))

        self.panel = wx.Panel(self)
        self.create_widgets()

    def create_widgets(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Текстовые поля для ввода чисел и операции
        self.num1_text = wx.TextCtrl(self.panel)
        self.num2_text = wx.TextCtrl(self.panel)
        self.operation_text = wx.TextCtrl(self.panel)

        # Кнопка для запуска операции
        self.calculate_button = wx.Button(self.panel, label="Calculate")

        # Текстовое поле для вывода результата
        self.result_text = wx.TextCtrl(self.panel, style=wx.TE_READONLY)

        # Размещение элементов на панели
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

        # Привязываем событие нажатия кнопки к методу calculate
        self.calculate_button.Bind(wx.EVT_BUTTON, self.calculate)

    def calculate(self, event):
        # Получаем введенные пользователем числа и операцию
        num1 = float(self.num1_text.GetValue())
        num2 = float(self.num2_text.GetValue())
        operation = self.operation_text.GetValue()

        # Выполняем операцию в зависимости от введенного символа
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Проверка деления на ноль
            if num2 == 0:
                self.result_text.SetValue("Error: Division by zero")
                return
            else:
                result = num1 / num2
        else:
            self.result_text.SetValue("Error: Invalid operation")
            return

        # Выводим результат
        self.result_text.SetValue(str(result))

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Calculator")
    frame.Show()
    app.MainLoop()