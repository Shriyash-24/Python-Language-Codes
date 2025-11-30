# User inputs...

import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.title("My Application")
window.minsize(400, 300)
custom_font = tkFont.Font(family="Times New Roman", size="15", weight="bold")

label = tk.Label(text="Hello World!", font=custom_font)
label.pack()

label["text"] = "Have a nice day!"

label.config(text = "My new app.")

count = 0
def function_button():
    global count
    count = count + 1
    label.config(text = f"The button got clicked {count} times.")

button = tk.Button(text="Click", command=function_button) # We don't see it yet, we need to use pack.
button.pack()

# Taking user input using Entry
# width is width of the input box, show masks the text.
user_input = tk.Entry(width=30)
user_input.pack()
print(user_input.get()) # We can get the user input from this but it runs before user does anything.

def user():
    input_text = user_input.get()
    label.config(text=input_text)

button2 = tk.Button(text="Click", command=user)
button2.pack()





window.mainloop()