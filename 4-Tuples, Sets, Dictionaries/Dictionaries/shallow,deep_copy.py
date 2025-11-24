import copy

l1 = [1, 2.5, [10,20,30], 'Python']

# Shallow Copy

l2 = copy.copy(l1)
print(l2)

# Variable will have memory address.
# Now shallow copy means different memory location.

print(id(l1), id(l2)) # 2061967151040 2061969491328
l1[0] = 100
print(l1, l2) # [100, 2.5, [10, 20, 30], 'Python'] [1, 2.5, [10, 20, 30], 'Python']

# Only l1 changed, not l2.

l1[2][0] = 50
print(l1, l2) # [100, 2.5, [50, 20, 30], 'Python'] [1, 2.5, [50, 20, 30], 'Python']

# Nested lists ~ l2 also changed here. Memory address of nested lists are same.

# Deep Copy ~ Inner elements also get copied at different memory locations.

l1 = [1,2.5,[10,20,30], 'Py']
l2 = copy.deepcopy(l1)
l1[0] = 5
l1[2][0] = 50
print(f"l1 --> {l1}", id(l1)) # l1 --> [5, 2.5, [50, 20, 30], 'Py'] 2685693492352
print(f"l2 --> {l2}", id(l2)) # l2 --> [1, 2.5, [10, 20, 30], 'Py'] 2685691023296

d1 = {'id': 1111, 'name': 'John', 'marks': {'eng':71.5, 'maths': 91.5, 'bio': 80.0}}
d2 = copy.copy(d1)
d1['name'] = "Dan"
d1['marks']['maths'] = 92.5
print(f"d1 --> {d1}", id(d1)) # d1 --> {'id': 1111, 'name': 'Dan', 'marks': {'eng': 71.5, 'maths': 92.5, 'bio': 80.0}} 2669636730176
print(f"d2 --> {d2}", id(d2)) # d2 --> {'id': 1111, 'name': 'John', 'marks': {'eng': 71.5, 'maths': 92.5, 'bio': 80.0}} 2669636730048

d1 = {'id': 1111, 'name': 'John', 'marks': {'eng':71.5, 'maths': 91.5, 'bio': 80.0}}
d2 = copy.deepcopy(d1)
d1['name'] = "Dan"
d1['marks']['maths'] = 92.5
print(f"d1 --> {d1}", id(d1)) # d1 --> {'id': 1111, 'name': 'Dan', 'marks': {'eng': 71.5, 'maths': 92.5, 'bio': 80.0}} 2400035323392
print(f"d2 --> {d2}", id(d2)) # d2 --> {'id': 1111, 'name': 'John', 'marks': {'eng': 71.5, 'maths': 91.5, 'bio': 80.0}} 2400035323456

