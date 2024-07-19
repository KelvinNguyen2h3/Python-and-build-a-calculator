import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Error","Invalid input! Please enter numbers only.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Error","Invalid input! Please enter numbers only.")
def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Error","Invalid input! Please enter numbers only.")
def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            result.set("Error! Division by zero.")
        else:
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Error","Invalid input! Please enter numbers only.")

root = tk.Tk()
root.title("Simple Calculator")
root.config(bg='lightblue')

tk.Label(root, text="Enter first number: ", bg='lightblue').grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root, font=('Arial', 14), borderwidth=2, relief="solid")
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number: ", bg='lightblue').grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root, font=('Arial', 14), borderwidth=2, relief="solid")
entry2.grid(row=1, column=1, padx=10, pady=5)

button_style = {
    'width': 10,
    'height': 2,
    'font': ('Arial', 14),
    'bg': 'orange',
    'fg': 'white'
}

tk.Button(root, text="Add", **button_style, command=add).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Subtract", **button_style, command=subtract).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Multiple", **button_style, command=multiply).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Divide", **button_style, command=divide).grid(row=3, column=1, padx=10, pady=5)

result = tk.StringVar()
tk.Label(root, text="Result: ", font=('Arial', 12), bg="lightblue").grid(row=4, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=result, font=('Arial', 13), borderwidth=2, relief="solid", state='readonly').grid(row=4, column=1, padx=10, pady=5)

root.mainloop()