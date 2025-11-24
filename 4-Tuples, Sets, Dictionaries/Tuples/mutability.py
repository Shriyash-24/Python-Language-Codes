# Mutability & Immutability
# Lists are mutable, Tuples and Strings are immutable.

s1 = "Python is fun"
s1.replace("Python","JavaScript")
print(s1) # Python is fun ( not changed )
# Doesn't modify existing string, but gives modified string which can be stored in another variable.
# Strings don't change their state after they are created.

t1 = ("Mango", "Orange", "Apple")
# t1.append("Banana") # Error
l1 = ["Mango", "Banana"]
l1.append("Orange")
print(l1) # ['Mango', 'Banana', 'Orange']

# So, strings and tuples are immutable, lists are mutable.

l2 = ["Mango", "Orange", "Apple"]
print(id(l2)) # 2246076553536
l2.append("Strawberry")
print(l2) # ['Mango', 'Orange', 'Apple', 'Strawberry']
print(id(l2)) # 2246076553536

# So, memory address is not changed in lists.

l3 = ["Mango", "Orange", "Aple"]
l3[-1] = "Apple" # Value can be changed using indexes.
print(l3) # ['Mango', 'Orange', 'Apple']
# This also comes under mutability ~ Memory addresses also remember same.

fruits = ("Mango", "Orange", "Aple")
# fruits[-1] = "Apple" # ERROR

s1 = "Python is fun"
s1[0] = 'p' # ERROR
