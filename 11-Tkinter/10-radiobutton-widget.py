import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Radiobutton Widget")
window.minsize(400, 300)

label = tk.Label(window, text="Radiobutton Widget")
label.pack()


# Radio buttons are useful when picking multiple options.
def get_radio_value():
    print(radio_value.get())

radio_value = tk.StringVar()
option_1 = ttk.Radiobutton(text="Male", variable=radio_value, value="Male", command=get_radio_value)
# Value argument is "What will be stored when Radio button is selected".
option_2 = ttk.Radiobutton(text="Female", variable=radio_value, value="Female", command=get_radio_value)

option_1.pack()
option_2.pack()





window.mainloop()
