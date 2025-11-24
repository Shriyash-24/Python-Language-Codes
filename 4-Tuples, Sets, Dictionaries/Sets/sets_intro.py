# Sets are non-sequential collection of items
# Comma separated elements enclosed within {}

s1 = {10,"Python", 2.5}
print(s1) # {10, 2.5, 'Python'}
print(type(s1)) # <class 'set'>

# We can have multiple data-types.
# print(s1[0]) # ERROR
# Indexing is not allowed in sets because they are non-sequential.
# Slicing is not allowed in sets as well.

print(len(s1)) # 3

# Sets are data structures that don't have duplicate elements.
s2 = {10,2,10}
print(s2) # {10, 2}

# Anything that is unique, should be stored in sets. Passport numbers, Aadhar number etc.

