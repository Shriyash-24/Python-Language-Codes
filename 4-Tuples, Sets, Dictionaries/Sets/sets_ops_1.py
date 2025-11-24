# Membership Operator - in, not in
nums = {1,3,2,0,-1}
print(0 in nums) # T
print(10 not in nums) # T

# Concatenation
nums_1 = {1,3,2,0,-1}
nums_2 = {3,5}
# print(nums_1 + nums_2) # ERROR

# Concatenation is not supported.

#print(nums_1 * 2) # ERROR
# Repetition is not supported.

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
weekdays = set(weekdays)
print(weekdays) # {'Wednesday', 'Tuesday', 'Thursday', 'Saturday', 'Monday', 'Sunday', 'Friday'}

# Sets are unordered, doesn't have any sequence. Everytime you run you get different order.

# Sets are mutable.
set1 = {2,0,-1}
# set1[0] = 10 # ERROR
# No indexing.

# add()
print(set1) # {0, 2, -1}
set1.add(5)
print(set1) # {0, 2, 5, -1}

set1.add(5)
print(set1) # {0, 2, 5, -1} ( No difference )

# remove()
print(set1) # {0, 2, 5, -1}
set1.remove(0)
print(set1) # {2, 5, -1}

# set1.remove(10) # ERROR ( Not part of set )

# discard() - Also deletes element.
set1.discard(5)
print(set1) # {2,-1}

set1.discard(10)
print(set1) # {2,-1} ~ No error given, unlike remove()

