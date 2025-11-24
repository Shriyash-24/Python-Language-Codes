from idlelib.autocomplete_w import LISTUPDATE_SEQUENCE

s1 = {"Maths": 80.5, "English": 76.0, "Physics": 89.0}
print(s1) # {'Maths': 80.5, 'English': 76.0, 'Physics': 89.0}

# How to fetch marks of physics?
print(s1["Physics"]) # 89.0
# print(s1["Chemistry"]) # ERROR

# get() ~ Fetches value in respect to key.
print(s1.get("Physics")) # 89.0
print(s1.get("Chemistry")) # No error and O/P is None
print(s1.get("Chemistry", 65.0)) # 65.0

emp1 = {'id':1001,'name':'John','salary':10000}
print(emp1.get('phone', 9876543210)) # 9876543210 (Default value)

# Membership Operator - in,not in
print(1001 in emp1) # F ( Present as value )
print('id' in emp1) # T ( Looks for key )

emp1['phone'] = 9876543210
print(emp1) # {'id': 1001, 'name': 'John', 'salary': 10000, 'phone': 9876543210}

sem1_marks = {'maths':78.5, 'English':71.0, "Physics":78.0}
sem2_marks = {'Chemistry':98.0, 'Biology':45.0}

# update() - Updates the key value pairs of another dictionary into the existing dictionary.
sem1_marks.update(sem2_marks)
print(sem1_marks) # {'maths': 78.5, 'English': 71.0, 'Physics': 78.0, 'Chemistry': 98.0, 'Biology': 45.0}
print(sem2_marks) # {'Chemistry': 98.0, 'Biology': 45.0}

groceries_1 = {'milk': 60,'rice': 100,'biscuits': 20}
groceries_2 = {'rice': 110,'bread': 30}
# Pay attention to rice.

groceries_1.update(groceries_2)
print(groceries_1) # {'milk': 60, 'rice': 110, 'biscuits': 20, 'bread': 30}

# Pop()
groceries_1.pop('milk')
print(groceries_1) # {'rice': 110, 'biscuits': 20, 'bread': 30}


groceries_1 = {'milk': 60,'rice': 100,'biscuits': 20, 'milk': 65}
print(groceries_1) # {'milk': 65, 'rice': 100, 'biscuits': 20}

# Keys can't be duplicated in a dictionary.

# More Operations

# d1 = {[1,3,5]: 9, [1,2,1]: 5} # Addition of values is the value of the dictionary.
# Keys can't be lists, error.
d1 = {"Nine":9, "Four": 4}
print(d1) # {'Nine': 9, 'Four': 4}

d1 = {1: True, 0: False}
print(d1) # {1: True, 0: False}

# Keys can be numbers.

d1 = {1.0: True, 0.0: False}
print(d1) # {1.0: True, 0.0: False}

# Keys can be float.

d1 = {True: 1, False: 0}
print(d1) # {True: 1, False: 0}

d1 = {(1,2,3):6, (1,2) :3}
print(d1) # {(1, 2, 3): 6, (1, 2): 3}

# d1 = {{1,2,3}: 6, {1,2}: 3}
# print(d1) # ERROR

# d1 = {{'a':1, 'b':2}: 6}
# print(d1) # ERROR

# Not Allowed Keys - Lists, Sets, Dictionaries --> Mutable
# Allowed keys - Strings ,Int, Float, Bool, Tuples --> Immutable4
# Values can be any datatype.

st1 = {'id': 1001, 'name': 'John', 'marks': [89.5, 71.5, 81.0]}
print(st1) # {'id': 1001, 'name': 'John', 'marks': [89.5, 71.5, 81.0]}
print(st1['marks']) # [89.5, 71.5, 81.0]
print(st1['marks'][0]) # 89.5

st1 = {'id': 1001, 'name': 'John', 'marks': {'eng': 89.5, 'maths': 78.0, 'physics': 78.0}}
print(st1['marks']) # {'eng': 89.5, 'maths': 78.0, 'physics': 78.0}
print(st1['marks']['eng']) # 89.5

# Fetch the keys or values? - keys(), values()
print(st1.keys()) # dict_keys(['id', 'name', 'marks'])
print(st1.values()) # dict_values([1001, 'John', {'eng': 89.5, 'maths': 78.0, 'physics': 78.0}])
print(st1.items()) # dict_items([('id', 1001), ('name', 'John'), ('marks', {'eng': 89.5, 'maths': 78.0, 'physics': 78.0})])

# Pairs are stored in tuple.





