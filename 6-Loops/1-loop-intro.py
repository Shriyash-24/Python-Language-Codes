# Loops - It is an iterator based loop which steps through the items of a collection,
# (lists, tuples, sets, dict, str) and executes a block ad code repeatedly for a number
# of items equal to the items/elements of that collection

l = ['Mike', 10.2, 1988]
for i in l:
    print(i)
# O/P -
# Mike
# 10.2
# 1988

# i stands for iteration. You can give anything there. It represents each element, for 1st iteration it represents Mike.
# For 2nd it represents 10.2 and so on.

for i in ['Mike', 10.2, 1988]:
    print(i)
# Same O/P ~ You can also use this way.

x = 'apple'
for i in x:
    print(i)
# O/P -
# a
# p
# p
# l
# e

# range()
for i in range(1,11):
    print(i)
# O/P -
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10