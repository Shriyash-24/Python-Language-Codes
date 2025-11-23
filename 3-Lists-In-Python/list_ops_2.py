# extend() - Adds element at end of the list.
# append() can add only one element at a time.

fruits = ["Apple", "Mango", "Orange"]
# fruits.append("Banana", "Grapes") # Error - Only 1 Argument
fruits.append(["Banana", "Grapes"])
print(fruits) # ['Apple', 'Mango', 'Orange', ['Banana', 'Grapes']]
fruits = ["Apple", "Mango", "Orange"]
fruits.extend(["Banana", "Grapes"])
print(fruits) # ['Apple', 'Mango', 'Orange', 'Banana', 'Grapes']

# remove()
fruits = ["Apple", "Mango", "Orange"]
fruits.remove("Mango")
print(fruits) # ['Apple', 'Orange']

fruits = ["Apple", "Mango", "Orange"]
# fruits.remove("Banana") # Error

fruits = ["Apple", "Mango", "Orange", "Mango"]
fruits.remove("Mango")
print(fruits) # 1st mango got deleted, second one got removed.

# pop() - It takes the index at which the value needs to be deleted.
fruits = ["Apple", "Mango", "Orange", "Mango"]
fruits.pop(2)
print(fruits) # ['Apple', 'Mango', 'Mango']
fruits.pop(-1)
print(fruits) # ['Apple', 'Mango']
fruits.pop()
print(fruits) # ['Apple'] ~ Last element was deleted.


