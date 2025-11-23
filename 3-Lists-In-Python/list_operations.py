# Slicing Of Lists

l1 = [3,8,1,0,4,9,7,3,6]
print(len(l1)) # 9
print(l1[1:6:1]) # [8, 1, 0, 4, 9]
print(l1[2:7:2]) # [1, 4, 7]

# Concatenation
l1 = [1,7,2]
l2 = [0,5]
print(l1 + l2) # [1, 7, 2, 0, 5]
print(l2 + l1) # [0, 5, 1, 7, 2]

# Repetition

print(l2 * 3) # [0, 5, 0, 5, 0, 5]

# append() - adds an item to the end of the list
# Syntax - list.append(item)

fruits = ["Mango", "Apple", "Orange"]
print(fruits) # ['Mango', 'Apple', 'Orange']
fruits.append("Banana")
print(fruits) # ['Mango', 'Apple', 'Orange', 'Banana']
print(fruits.append("Strawberry")) # None ( So we can't directly print functions in lists. )
# Because, we are changing the same list.
print(fruits)  # ['Mango', 'Apple', 'Orange', 'Banana', 'Strawberry']

# insert() - Adds an element before the specified index.
# Syntax - list.insert(index, item)

phal = ["Mango", "Apple", "Orange"]
phal.insert(2, "Banana")
print(phal) # ['Mango', 'Apple', 'Banana', 'Orange']



