import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Checkbutton")
window.minsize(400, 300)

label = tk.Label(text="Hello World")
label.pack()

# check_option = tk.IntVar()  # IntVar() is used for integers.
check_option = tk.StringVar() # To have strings such as Yes or No when the checkbutton is checked or not

def check_option_task():
    print(check_option.get())

# Used for "Agreeing to terms and conditions.
check_button = ttk.Checkbutton(text="Checkbutton", variable=check_option, command=check_option_task, onvalue="Yes", offvalue="No")
#
check_button.pack()




window.mainloop()