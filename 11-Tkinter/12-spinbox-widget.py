import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.minsize(300, 200)

label = tk.Label(window, text="Spinbox Widget")
label.pack()

# Spinbox
def get_spin_box_value():
    print(f"Spinbox Value: {spin_box.get()}")
counter = tk.IntVar(value=10) # Used to bring initial value

spin_box = ttk.Spinbox(from_=0, to=20, textvariable=counter, wrap=True, command=get_spin_box_value)
# value=(10,15,20,25) ~ Only 10,15,20,25 will be reflected in the counter.
# values= tuple(range(5,105,5)) ~ Interval of 5 till 105.
# wrap is used when you need to reset value when you do minimum or maximum values, goes circular counting.
spin_box.pack()




window.mainloop()