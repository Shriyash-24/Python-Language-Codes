# Tuple - We write element in round brackets.
# Sequence of items as a collection.
# (item1, item2, ....)
# We can't modify, delete, insert elements in tuple. Elements are fixed.
# Tuples can be used ~ For eg - Storing the months of the year. Can we change this? - No.
# Tuples are used where we don't need to modify anything. There's no scope of modification.
# Any data type can be used in a tuple.

t1 = ("Python", 10, 1.5, True, [1,2,4], (10,20))
print(t1) # ('Python', 10, 1.5, True, [1, 2, 4], (10, 20))
print(len(t1)) # 6

# Accessing elements in a tuple - indexing
print(t1[0]) # Python
print(t1[-1]) # (10,20)

t2 = (10,20,30)
print(t2) # (10, 20, 30)
print(type(t2)) # <class 'tuple'>

t3 = 10,30,40
print(t3) # (10, 30, 40)
print(type(t3)) # <class 'tuple'>
# Parenthesis is optional.

l1 = [1,2,3]
print(type(l1)) # <class 'list'>
t1 = tuple(l1)
print(t1) # (1,2,3)
print(type(t1)) # <class 'tuple'>

fruits = ("Mango", "Orange", "Apple")
print(fruits,type(fruits)) # ('Mango', 'Orange', 'Apple') <class 'tuple'>
fruits = list(fruits)
print(fruits,type(fruits)) # ['Mango', 'Orange', 'Apple'] <class 'list'>
