# Themed tk - ttk.

import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("My App.")
window.minsize(300, 300)

label = ttk.Label(window, text="Hello World.")
label.pack()

user_input = ttk.Entry(width=30)
user_input.pack()

def user():
    ip = user_input.get()
    label.config(text=ip)

button = ttk.Button(text="Click Me!", command=user)
button.pack()

window.mainloop()