# After the label creation, we want to change the text to something else.

import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.title("My Application")
window.minsize(400, 300)
custom_font = tkFont.Font(family="Times New Roman", size="15", weight="bold")

label = tk.Label(text="Hello World!", font=custom_font)
label.pack()

# Changing text.
label["text"] = "Have a nice day!"
# Config method is change the parameters of the label class.
label.config(text = "My new app.")

# Buttons - CLickable content in my app.
# command can take a function name. No need to call it.
# How many times button got clicked?
count = 0
def function_button():
    global count
    count = count + 1
    label.config(text = f"The button got clicked {count} times.")

button = tk.Button(text="Click", command=function_button) # We don't see it yet, we need to use pack.
button.pack()



window.mainloop()