# Comma separated key-value pairs enclosed within {}.
# {key1:value1, key2:value2}

groceries = {'milk':60, 'biscuits':20, 'rice':90, 'bread':30}
print(groceries, type(groceries)) # {'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 30} <class 'dict'>
print(len(groceries)) # 4 ~ 4 key value pairs present in dictionary.

# print(groceries[0]) # ERROR ~ Indexing is not allowed.
print(groceries['milk']) # 60 ~ Basically give the key to fetch its value.

# DICTIONARIES ARE MUTABLE
groceries['milk'] = 65 # Updates the value of key if present
print(groceries) # {'milk': 65, 'biscuits': 20, 'rice': 90, 'bread': 30}

# print(groceries['chips']) # ERROR ~ Not present in dictionary.
groceries['chips'] = 10 # Adds new key-value pair if not present.
print(groceries) # {'milk': 65, 'biscuits': 20, 'rice': 90, 'bread': 30, 'chips': 10}

