import tkinter as tk
from tkinter import messagebox

def click(event):
    entry.insert(tk.END, event)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error",f"Invalid value: {e}")

root = tk.Tk()
root.title("Simple Calculator")
root['bg'] = 'black'

entry = tk.Entry(root, width=16, font=('Arial',24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+',
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click(x) if x != "=" else calculate()
    tk.Button(root, text=button, width=5, height=2, font=('Arial',18), bg='yellow', command=action).grid(row=row_val, column=col_val)
    col_val +=1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', width=22, height=2, font=('Arial',18), bg='yellow', command=clear).grid(row=row_val, column=col_val, columnspan=4)

root.mainloop()
