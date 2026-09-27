"""
Simple Calculator Application
Course: COU3303 - Software Engineering
Author: <your name here>

A basic GUI calculator built with Python's Tkinter library.
Supports addition, subtraction, multiplication, division,
decimal numbers, clear, and backspace.

Run with:
    python calculator.py
"""

try:
    import tkinter as tk
except ImportError:
    tk = None  # GUI unavailable; core functions below still work for testing


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(False, False)

        # Expression currently being built, and the text shown on screen
        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_display()
        self._build_buttons()

    # ---------- UI ----------
    def _build_display(self):
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.RIDGE,
            state="readonly",
            readonlybackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=15)

    def _build_buttons(self):
        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2, 2),
        ]

        for spec in buttons:
            text, row, col = spec[0], spec[1], spec[2]
            colspan = spec[3] if len(spec) > 3 else 1
            btn = tk.Button(
                self.root,
                text=text,
                font=("Arial", 18),
                command=lambda t=text: self.on_button(t),
            )
            btn.grid(
                row=row, column=col, columnspan=colspan,
                sticky="nsew", ipady=10
            )

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    # ---------- Logic ----------
    def on_button(self, char):
        if char == "C":
            self.clear()
        elif char == "⌫":
            self.backspace()
        elif char == "=":
            self.calculate()
        else:
            self.expression += char
            self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("0")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression if self.expression else "0")

    def calculate(self):
        try:
            result = evaluate_expression(self.expression)
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("Error: Div by 0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""


def evaluate_expression(expr: str):
    """
    Safely evaluate a simple arithmetic expression containing
    only numbers and the operators + - * / %.
    Raises ZeroDivisionError on division by zero.
    Raises ValueError on an invalid/empty expression.
    """
    allowed = set("0123456789.+-*/% ")
    if not expr or not set(expr).issubset(allowed):
        raise ValueError("Invalid expression")

    # eval is safe here because input is restricted to digits/operators above
    result = eval(expr, {"__builtins__": {}})
    return result


# ----- Standalone functions used directly by the automated test cases -----
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    if tk is None:
        print("tkinter is not available on this system. "
              "Install it to run the GUI (e.g. 'sudo apt install python3-tk').")
    else:
        root = tk.Tk()
        app = Calculator(root)
        root.mainloop()
