import tkinter as tk
import tkinter.font as tFont

window = tk.Tk()
window.title("My Application")

# Label
label = tk.Label(text="Hello World!") # Nothing is visible when we run
# We need pack method for it.
label.pack() # Text is place but window became slower just to display the text.

# Minimum size of the application ~ minsize
window.minsize(width=400,height=600)

# We can change the font of message too.
label = tk.Label(text="Hello World!", font=("Times New Roman", 20, "bold"))
label.pack()

# Custom Font
custom_font = tFont.Font(family="Times New Roman", size=15, slant='italic', weight='bold')
label = tk.Label(text="Hello World!", font=custom_font)

# Label pack methods
# side = top/left/right/bottom/
# expand = True means center it.
label.pack(expand=True)

# Configuring the label later?
label.config(font=("Courier New", 25, "underline"))



window.mainloop()