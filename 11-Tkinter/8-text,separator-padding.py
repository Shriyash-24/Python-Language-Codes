import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("My App.")
window.minsize(300, 300)

label = ttk.Label(window, text="Hello World.", padding=15) # padding here worked on labels.
label.pack()

user_input = ttk.Entry(width=30)
user_input.pack()

def user():
    ip = user_input.get()
    label.config(text=ip)

button = ttk.Button(text="Click Me!", command=user)
button.pack()

# Quit Button
quit_button = ttk.Button(text="Quit", command=window.destroy)
quit_button.pack(pady=10) # pady provided some padding up and down/

sep = ttk.Separator(orient="horizontal") # It has created but only 1 pixel
sep.pack(fill = 'x')

# Writing the text in multiple lines.
text = tk.Text(height=5, width=25)
text.pack(pady=10) # Y axis padding is done.
text.focus() # Make the cursor go inside the box.

# Default text in the textbox.
# 1.0 is positional argument, 1 means first line, .0 means first character.
text.insert("1.0", "Enter your comments")

# get method fetches part or entire text.
# 1.0 is starting position, for ending position you can write end.

def data_fetch():
    text_data = text.get("1.0", "end")
    label.config(text=text_data)

button_fetch = ttk.Button(text="Fetch", command=data_fetch)
button_fetch.pack()


# # Disable textbox or any component.
# text["state"] = "disabled" # Can't do anything in text.
#
# # Enable text button function.
# def enable_text():
#     text["state"] = "normal"
#
# # Enable textbox button.
# enable_button = ttk.Button(text="Enable", command=enable_text)
# enable_button.pack()

# Separator Widget - For readability of the widget. Provides separtors between widgets.
# Go to line 25.

# Padding
# Go to line 12, 23, 30.



window.mainloop()