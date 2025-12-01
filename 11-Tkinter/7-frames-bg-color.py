# Frame is something that provides more flexibility while layout the components in the window.
import tkinter as tk
from tkinter import ttk

window = tk.Tk() # Root Window.
window.title("My App.")

# Added later.
my_frame = ttk.Frame()
my_frame.pack(side="left", fill="both", expand=True)


# bg lets us set background color of our label.
# Frame creates a sub window.
label1 = tk.Label(my_frame,text="Hello World.", bg="red")
label1.pack(side="left", fill="both", expand=True)
# fill = y  takes entire vertical space
# fill = x doesn't change anything because side=left was there.
# fill = x, expand = True.. if window grows component grows.
# fill = both, expand = True.. utilize x and y space.

label2 = tk.Label(window, text="How are you?", bg="blue")
# fill=both, expand=True was added later, after line 14.
label2.pack(side="left", fill="both", expand=True)

label3 = tk.Label(window, text="Have a nice day.", bg="green")
# fill=both, expand=True was added later, after line 14.
label3.pack(side="left", fill="both", expand=True)

window.mainloop()