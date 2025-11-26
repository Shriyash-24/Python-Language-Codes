# filter(function, sequence) - Leverages lambda function

seq = [1,2,3,4]
odd = lambda x : True if x % 2 != 0 else False
filtered_op = filter(odd,seq)
print(filtered_op) # <filter object at 0x000001D3EA905150>

# Either run a for loop or convert it to a list
print(list(filtered_op)) # [1,3]
"""
For each element of seq, filter function will call odd function.
add(1) - True - keeps 1
add(2) - False - discard 2
add(3) - True - keep 3
add(4) - False - discard 4
"""

# map() - Takes function as 1st argument and sequence as 2nd argument.
seq = [1,2,3,4]
odd = lambda x : True if x % 2 != 0 else False
mapped_op = map(odd,seq)
print(list(mapped_op)) # Keeps output ~ [True, False, True, False]
