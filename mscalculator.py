import tkinter as tk
from tkinter import messagebox
import math
class BasicCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimalist Simple Calculator")
        self.root.geometry("400x500")
        self.bg_variants = ["white", "black", "gray90", "gray10", "snow", "ivory"]
        self.bg_index = 0
        self.root.configure(bg=self.bg_variants[self.bg_index])
        self.expression = ""
        self.input_text = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        self.top_bar = tk.Frame(self.root, bg=self.root["bg"])
        self.top_bar.pack(fill=tk.X, side=tk.TOP)
        self.theme_btn = tk.Button(self.top_bar, text="☽", font=('Times New Roman', 14), bg=self.root["bg"], fg="black",
                                   bd=0, command=self.toggle_background)
        self.theme_btn.pack(side=tk.RIGHT, padx=10, pady=5)
        self.input_frame = tk.Frame(self.root, bg=self.root["bg"])
        self.input_frame.pack(pady=10)
        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('Arial', 24, 'bold'),
                                    bd=10, insertwidth=4, width=14, justify='right', bg="white", fg="black")
        self.input_field.pack()
        self.buttons_frame = tk.Frame(self.root, bg=self.root["bg"])
        self.buttons_frame.pack()
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('%', 5, 3),
            ('//', 6, 0), ('π', 6, 1), ('^', 6, 2), ('√', 6, 3)
        ]
        for (text, row, col) in buttons:
            color = self.get_hover_color(text)
            btn = tk.Button(self.buttons_frame, text=text, width=5, height=2, font=('Arial', 18, 'bold'),
                            bg="black", fg="white", command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="black"))
    def get_hover_color(self, text):
        if text in {'+', '-', '*', '/', '=', '^', '√', '%', '//'}:
            return "blue"
        elif text == 'C':
            return "red"
        else:
            return "green"
    def button_click(self, item):
        try:
            if item == '=':
                expression = self.expression.replace('π', 'math.pi').replace('√', 'math.sqrt')
                result = str(eval(expression, {"__builtins__": None}, {"math": math}))
                self.input_text.set(result)
                self.expression = result
            elif item == 'C':
                self.clear()
            elif item == '√':
                self.expression += 'math.sqrt('
            elif item == '^':
                self.expression += '**'
            elif item == 'π':
                self.expression += 'math.pi'
            else:
                self.expression += item
            self.input_text.set(self.expression)
        except Exception:
            self.input_text.set("Error")
            self.root.after(1000, self.clear)
    def clear(self):
        self.expression = ""
        self.input_text.set("")
    def toggle_background(self):
        self.bg_index = (self.bg_index + 1) % len(self.bg_variants)
        new_bg = self.bg_variants[self.bg_index]
        self.root.configure(bg=new_bg)
        self.top_bar.configure(bg=new_bg)
        self.input_frame.configure(bg=new_bg)
        self.buttons_frame.configure(bg=new_bg)
        self.theme_btn.configure(bg=new_bg)
        self.theme_btn.configure(text="꥟" if new_bg in ["black", "gray10"] else "☽")
if __name__ == "__main__":
    root = tk.Tk()
    app = BasicCalculator(root)
    root.mainloop()