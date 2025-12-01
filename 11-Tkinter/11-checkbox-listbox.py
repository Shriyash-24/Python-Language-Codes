import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My first window")
window.minsize(400, 300)

label = tk.Label(window, text="My first label")
label.pack()

# Combo Box

# What is event?
def combo_box_function(event):
    label2 = tk.Label(text=f"Selected Option: {combo_str.get()}")
    label2.pack()

combo_str = tk.StringVar()
countries = ttk.Combobox(textvariable=combo_str, values=("Australia", "Canada", "France", "Italy", "India"))
# When we run upper code,we can write on the combobox.
countries["state"] = "readonly"
countries.bind("<<ComboboxSelected>>", combo_box_function) # Used to bind combo box to a function.
countries.pack()


# Listbox - We have to choose from options, but multi-select and all options can be visible.
food_items = ("Pizza", "Burger", "Garlic Bread", "Nachos", "Salad")
fav_food = tk.StringVar(value=food_items)
food_list = tk.Listbox(listvariable=fav_food, height=5, selectmode="extended")
food_list.pack()

def get_fav_food(event):
    food_indices = food_list.curselection() # you get indices of selected items
    for i in food_indices:
        print(food_list.get(i))
food_list.bind("<<ListboxSelect>>", get_fav_food)

window.mainloop()