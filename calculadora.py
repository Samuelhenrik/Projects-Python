import tk


import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("230x160")
        self.title("Calculadora")

        self.entry = tk.Entry(self, width=10)
        self.entry.grid(row=10, column=10, columnspan=4)

        buttons = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
            ("0", 4, 0)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self, text=text, command=lambda t=text: self.entry.insert(tk.END, t))
            button.grid(row=row, column=column)

        operators = ["+", "-", "*", "/"]
        for i, operator in enumerate(operators):
            button_operator = tk.Button(self, text=operator, command=lambda o=operator: self.entry.insert(tk.END, o))
            button_operator.grid(row=i + 1, column=3)

        button_equal = tk.Button(self, text="=", command=self.calculate)
        button_equal.grid(row=4, column=2)

        button_clear = tk.Button(self, text="C", command=self.clear)
        button_clear.grid(row=4, column=1)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Erro")

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()


    def calculate(self):
        try:
            expressao = self.entry.get()
            resultado = eval(expressao)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(resultado))
        except (SyntaxError, ZeroDivisionError, ValueError):
            # Lidar com exceções específicas
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Erro")