import random

# random() - return random float between 0.0 and 1.0 ( excluded )
print(random.random()) # 0.5019199268126928 (random value changes everytime)

# randint(a,b) --> returns random int between a and b (both included)
print(random.randint(10,15)) # 15 ( random value )

nums = [10,4,1,8,4,3]
# choice(sequence) - returns a random item from the sequence.
print(random.choice(nums)) # 8 ( Returns value from sequence )

# shuffle(sequence) - Returns elements shuffled in random order.

fruits = ["apple", "banana", "cherry"]
print(random.shuffle(fruits)) # None ( Doesn't print anything )
random.shuffle(fruits)

print(fruits) # ['banana', 'cherry', 'apple']

