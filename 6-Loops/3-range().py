# Range - Built-in function used to generate sequence of integers in a given interval
# range(start,stop,step)

"""
for i in range(start, stop, step):
    # statements
"""

for i in range(1,10,1):
    print(i) # 1,2,3....9

for i in range(1,11,1):
    print(i) # 1,2,3...10

for i in range(1,11,2):
    print(i) # 1,3,5,7,9

for i in range(2,11,2):
    print(i) # 2,4,6,8,10

# Reverse Order - 20 to 10 (excluding 10)
for i in range(20,10,-1):
    print(i) # 20,19,18..11

for i in range(20,10,-2):
    print(i) #20,18,16,14,12

# Countdown from 10 to 1 (including 1)
for i in range(10,0,-1):
    print(i) # 10,9,8...1

# range(start,stop) ==> step is 1 by default.
for i in range(1,5):
    print(i) # 1,2,3,4

for i in range(5):
    print(i) # 0,1,2,3,4

# start = 0 is by default in upper case.

groceries = ['salt','milk','sugar']
# Index -      0       1       2
# We are not fetching indexes, only values.
for item in groceries:
    print(item) # salt, milk, sugar

# How to fetch indexes?
for index in range(0, len(groceries)):
    print(index) # 0,1,2

profits  = [9,11,6,10]
# O/P I want - Profit of Quarter 1 is 9 & so on..

for index in range(len(profits)):
    q = index + 1
    print(f"Profit of Quarter is {q} is {profits[index]}")





